from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import HarmfulIngredient

admin.site.register(HarmfulIngredient)

# modification of the Admin.py
