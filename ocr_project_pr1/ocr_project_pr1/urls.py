"""
URL configuration for ocr_project_pr1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ocr_app_pr1.views import upload_and_scan_image
from ocr_app_pr1.views import *
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload_and_scan_image', upload_and_scan_image, name='upload_and_scan_image'),
    path('About',About, name='About'),
    path('Contact', Contact, name = 'Contact'),
    path('', Home, name= 'Home'),
    path('Ingredient', Ingredient, name = 'Ingredient'),
    path('index', index, name = 'index')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
