from django.urls import path
from .views import leads_list, leads_detail

app_name = 'leads'

urlpatterns = [
    path('', leads_list, name='lead-list'),
    path('<int:pk>/', leads_detail, name='lead-detail'),
]