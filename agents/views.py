from typing import Any
from django.core.mail import send_mail
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import AgentModelForm
from leads.models import Agent

def logoutview(request):
    logout(request)
    return redirect('landing-page')


class AgentListView(LoginRequiredMixin, ListView):
    template_name = 'agents/agent_list.html'
    
    context_object_name = 'agents'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    
    


class AgentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'agents/agent_detail.html'
    
    context_object_name = 'agents'
    def get_queryset(self):
        return Agent.objects.all()


class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm
    

    def get_success_url(self):
        return reverse("agents:agent-list")  
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)
    

class AgentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm
    context_object_name = 'agents'

    def get_queryset(self):
        return Agent.objects.all()

    def get_success_url(self):
        return reverse("agents:agent-list")


class AgentDeleteView(LoginRequiredMixin, DeleteView):
  
    template_name = 'agents/agent_delete.html'

    def get_queryset(self):
        return Agent.objects.all()

    def get_success_url(self):
        return reverse("agents:agent-list")
    
    
    