from rest_framework import generics
from .models import Equipment
from .serializers import EquipmentSerializer
from rest_framework.permissions import IsAdminUser

class EquipmentCreateView(generics.CreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAdminUser]

class EquipmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAdminUser] 

class EquipmentListView(generics.ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAdminUser]
