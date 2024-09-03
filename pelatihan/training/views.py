from django.shortcuts import render
from rest_framework import generics
from .models import Training
from .serializers import TrainingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class TrainingListCreateView(generics.ListCreateAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    # permission_classes = [IsAuthenticated]

class TrainingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    # permission_classes = [IsAuthenticated]
