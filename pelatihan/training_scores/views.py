from django.shortcuts import render
from rest_framework import generics, permissions
from .models import TrainingScore
from .serializers import TrainingScoreSerializer

# Create your views here.
class TrainingScoreListView(generics.ListAPIView):
    serializer_class = TrainingScoreSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return TrainingScore.objects.all()
        else:
            return TrainingScore.objects.filter(user=user)

    def get_permissions(self):
        if self.request.user.role == 'admin' or self.request.user.role == 'user':
            return [permissions.IsAuthenticated()]
        return []
