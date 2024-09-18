from django.db import models

# Create your models here.
# models.py

from django.db import models

class HarmfulIngredient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    class meta:
        db_table = "HarmfulIngredient"



from django.db import models

# Create your models here.

class Harmful_Ingredients(models.Model):
    HARM_LEVEL_CHOICES = {
        'select': 'Select',
        'low': 'Low',
        'medium': 'Medium',
        'high': 'High',
    }
    ingredient= models.CharField(max_length = 150)
    desc = models.TextField()
    Harm_Level= models.CharField(max_length=10, choices=HARM_LEVEL_CHOICES, default= 'select')
    class Meta:
        db_table = 'Harmful_Ingredients'

class product_type(models.Model):
    product_name = models.CharField(max_length = 150)
    product_image = models.ImageField(upload_to='products/')
    product_link = models.URLField()
    class Meta:
        db_table = 'product_type'