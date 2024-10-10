from django.urls import path
from .views import EstimateCreateView, EstimateDetailView

urlpatterns = [
    path('estimate/', EstimateCreateView.as_view(), name='create-estimate'),
    path('estimate/<int:pk>/', EstimateDetailView.as_view(), name='estimate-detail'),
]