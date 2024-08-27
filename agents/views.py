import random
from typing import Any
from django.core.mail import send_mail
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import AgentModelForm
from leads.models import Agent
from .mixins import OrganisorAndLoginRequiredMixin
def logoutview(request):
    logout(request)
    return redirect('landing-page')


class AgentListView(OrganisorAndLoginRequiredMixin, ListView):
    template_name = 'agents/agent_list.html'
    
    context_object_name = 'agents'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    
    


class AgentDetailView(OrganisorAndLoginRequiredMixin, DetailView):
    template_name = 'agents/agent_detail.html'
    
    context_object_name = 'agents'
    def get_queryset(self):
        return Agent.objects.all()


class AgentCreateView(OrganisorAndLoginRequiredMixin, CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm
    

    def get_success_url(self):
        return reverse("agents:agent-list")  
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password(f"random.randint(0,100000)")
        user.save()
        Agent.objects.create(user=user, organisation = self.request.user.userprofile)
        send_mail(
            subject="You are invited to be an agent",
            message="You were added as an agent on DJCRM. Please come login to start working.",
            from_email="admin@test.com",
            recipient_list=[user.email]
        )
        return super(AgentCreateView, self).form_valid(form)
    

class AgentUpdateView(OrganisorAndLoginRequiredMixin, UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm
    context_object_name = 'agents'

    def get_queryset(self):
        return Agent.objects.all()

    def get_success_url(self):
        return reverse("agents:agent-list")


class AgentDeleteView(OrganisorAndLoginRequiredMixin, DeleteView):
  
    template_name = 'agents/agent_delete.html'

    def get_queryset(self):
        return Agent.objects.all()

    def get_success_url(self):
        return reverse("agents:agent-list")
    
    
    