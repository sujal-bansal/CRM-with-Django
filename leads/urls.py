from django.urls import path
from .views import leads_list

app_name = 'leads'

urlpatterns = [
    path('', leads_list, name='lead-list')
]