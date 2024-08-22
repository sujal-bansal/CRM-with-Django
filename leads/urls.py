from django.urls import path
from .views import (leads_list, leads_detail, leads_create, leads_update, 
                    leads_delete, LeadDetailView, LeadListView, LeadCreateView, LeadUpdateView, LeadDeleteView
)
app_name = 'leads'

urlpatterns = [
    path('',  LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('update/<str:pk>',LeadUpdateView.as_view(), name='lead-update'),
    path('delete/<str:pk>', LeadDeleteView.as_view(), name='lead-delete'),
]