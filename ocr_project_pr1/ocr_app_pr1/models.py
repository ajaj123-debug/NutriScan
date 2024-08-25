from django.db import models

# Create your models here.
# models.py

from django.db import models

class HarmfulIngredient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
