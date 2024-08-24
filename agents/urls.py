from django.urls import path
from .views import ( AgentDetailView, AgentListView, AgentCreateView, AgentUpdateView, AgentDeleteView
)
app_name = 'agents'

urlpatterns = [
    path('',  AgentListView.as_view(), name='agent-list'),
    path('<int:pk>/', AgentDetailView.as_view(), name='agent-detail'),
    path('create/', AgentCreateView.as_view(), name='agent-create'),
    path('update/<str:pk>',AgentUpdateView.as_view(), name='agent-update'),
    path('delete/<str:pk>', AgentDeleteView.as_view(), name='agent-delete'),
]