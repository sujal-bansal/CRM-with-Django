from typing import Any
from django.core.mail import send_mail
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView
from agents.mixins import OrganisorAndLoginRequiredMixin
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm
from .models import Lead, Agent


def logoutview(request):
    logout(request)
    return redirect('landing-page')



class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self) -> str:
        return reverse('login')



class LandingPageView(LoginRequiredMixin, TemplateView):
    template_name = 'landing.html'


class LeadListView(LoginRequiredMixin, ListView):
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'

    
    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation = user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation = user.agent.organisation)
            queryset = queryset.filter(agent__user = user)
        return queryset


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = 'leads/lead_detail.html'
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation = user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation = user.agent.organisation)
            queryset = queryset.filter(agent__user = user)
        return queryset


class LeadCreateView(OrganisorAndLoginRequiredMixin, CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm
    

    def get_success_url(self):
        return reverse("leads:lead-list")  
    
    def form_valid(self, form):
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead",
            from_email = "test@test.com",
            recipient_list=['test2@test.com']
        )
        return super(LeadCreateView, self).form_valid(form)
    

class LeadUpdateView(OrganisorAndLoginRequiredMixin, UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation = user.userprofile)

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadDeleteView(OrganisorAndLoginRequiredMixin, DeleteView):
    template_name = 'leads/lead_delete.html'

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation = user.userprofile)

    def get_success_url(self):
        return reverse("leads:lead-list")
    




def landing_page(request):
    return render(request, 'landing.html')


def leads_list(request):
    leads = Lead.objects.all()

    context = {'leads' : leads}

    return render(request, "leads/lead_list.html", context)



def leads_detail(request, pk):
    leads = Lead.objects.get(id = pk)

    context = {'leads' : leads}

    return render(request, "leads/lead_detail.html", context)


def leads_create(request):
    form = LeadModelForm()
    
    if request.method == "POST":

        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            print("This long and lenghty manual submission of a new lead is sucessful")

            return redirect('leads:lead-list')
        
    context = {"form" :form}
    return render(request, "leads/lead_create.html", context)



    

def leads_update(request, pk):
    lead = Lead.objects.get(id= pk)
    form = LeadModelForm(instance=lead)
    
    if request.method == "POST":

        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('leads:lead-list')
        
    context = {"form" :form, "leads" : lead }
    return render(request, "leads/lead_update.html", context)


    

def leads_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()

    return redirect('leads:lead-list')


# def leads_create(request):
#     form = LeadForm()
    
#     if request.method == "POST":

#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first() 

#             Lead.objects.create(
#                 first_name = first_name,
#                 last_name = last_name,
#                 age = age,
#                 agent = agent
#             )

#             print("This long and lenghty manual submission of a new lead is sucessful")

#             return redirect('leads:lead-list')
        
#     context = {"form" :form}
#     return render(request, "leads/lead_create.html", context)
