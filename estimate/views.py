from rest_framework import generics
from .models import Estimate
from .serializers import EstimateSerializer

class EstimateCreateView(generics.CreateAPIView):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer

class EstimateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer