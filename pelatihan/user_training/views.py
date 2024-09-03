from django.shortcuts import render
from rest_framework import generics, permissions
from .models import UserTraining
from .serializers import UserTrainingSerializer

# Create your views here.
class UserTrainingListView(generics.ListAPIView):
    serializer_class = UserTrainingSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.BasePermission]

    def get_queryset(self):
        return UserTraining.objects.filter(user=self.request.user)

    # def get_permissions(self):
    #     user_role = self.request.user.role
    #     if user_role != 'user':
    #         return [permissions.Denied()]
    #     return super().get_permissions()

class UserTrainingDetailView(generics.RetrieveAPIView):
    serializer_class = UserTrainingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise permissions.PermissionDenied("You do not have permission to access this resource.")
        return obj
