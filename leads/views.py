from django.shortcuts import render
from django.http import HttpResponse

from .models import Lead

def leads_list(request):
    leads = Lead.objects.all()

    context = {'leads' : leads}

    return render(request, "leads/listpage.html", context)


def leads_detail(request, pk):
    return HttpResponse('Here is the detail view')


