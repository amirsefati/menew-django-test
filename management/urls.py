from django.urls import path
from .views import EquipmentCreateView, EquipmentDetailView, EquipmentListView

urlpatterns = [
    path('equipment/', EquipmentListView.as_view(),
         name='equipment-list'),
    path('equipment/create/', EquipmentCreateView.as_view(),
         name='equipment-create'),
    path('equipment/<int:pk>/', EquipmentDetailView.as_view(),
         name='equipment-detail'),
]
