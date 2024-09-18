from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import *

admin.site.register(HarmfulIngredient)
admin.site.register(product_type)
admin.site.register(Harmful_Ingredients)
