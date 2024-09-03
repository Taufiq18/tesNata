from rest_framework import serializers
from .models import TrainingScore

class TrainingScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingScore
        fields = ['id', 'user', 'training', 'score']
