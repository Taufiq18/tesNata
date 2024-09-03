from django.db import models

# Create your models here.
class Training(models.Model):
    CATEGORIES = [
        ('informasi_teknologi', 'Informasi Teknologi'),
        ('marketing', 'Marketing'),
        ('bisnis', 'Bisnis'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    mentor = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name