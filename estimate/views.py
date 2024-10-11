from rest_framework import generics
from .models import Estimate
from .serializers import EstimateSerializer
from rest_framework.permissions import IsAdminUser

class EstimateCreateView(generics.CreateAPIView):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
    permission_classes = [IsAdminUser]

class EstimateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
    permission_classes = [IsAdminUser]
