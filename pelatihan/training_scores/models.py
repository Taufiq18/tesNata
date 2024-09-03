from django.db import models
from django.conf import settings
from training.models import Training

# Create your models here.
class TrainingScore(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        ordering = ['-score', 'training__name']

    def __str__(self):
        return f"{self.user.username} - {self.training.name} - {self.score}"