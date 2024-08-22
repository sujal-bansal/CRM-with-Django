from django.shortcuts import render

from .models import Lead

def leads_list(request):
    leads = Lead.objects.all()

    context = {'leads' : leads}

    return render(request, "leads/listpage.html", context)
