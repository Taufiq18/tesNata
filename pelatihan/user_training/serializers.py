from rest_framework import serializers
from .models import UserTraining
from training.serializers import TrainingSerializer

class UserTrainingSerializer(serializers.ModelSerializer):
    training = TrainingSerializer()

    class Meta:
        model = UserTraining
        fields = ['id', 'training', 'date_joined']
