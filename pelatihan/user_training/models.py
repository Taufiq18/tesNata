from django.db import models
from django.conf import settings
from training.models import Training

# Create your models here.
class UserTraining(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'training')  # Ensure a user can't follow the same training more than once

    def __str__(self):
        return f"{self.user.username} - {self.training.name}"