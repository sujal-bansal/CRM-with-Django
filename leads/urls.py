from django.urls import path
from .views import (leads_list, leads_detail, leads_create, leads_update, 
                    leads_delete, LeadDetailView, LeadListView, LeadCreateView, 
                    LeadUpdateView, LeadDeleteView, AssignAgentView, CategoryListView
)
app_name = 'leads'

urlpatterns = [
    path('',  LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('assign/<str:pk>', AssignAgentView.as_view(), name='assign-agent'),
    path('update/<str:pk>',LeadUpdateView.as_view(), name='lead-update'),
    path('delete/<int:pk>', LeadDeleteView.as_view(), name='lead-delete'),
    path('category', CategoryListView.as_view(), name="category-list")
]