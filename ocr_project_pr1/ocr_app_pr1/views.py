from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import pytesseract
from PIL import Image
from .models import HarmfulIngredient  # Import the HarmfulIngredient model
import os

# Set the Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def upload_and_scan_image(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')

        if not uploaded_file:
            return JsonResponse({'error': 'No file uploaded'}, status=400)

        # Create a path in the media directory
        file_name = uploaded_file.name
        file_path = default_storage.save(f'temp/{file_name}', ContentFile(uploaded_file.read()))

        try:
            # Perform OCR processing on the image
            with default_storage.open(file_path) as image_file:
                extracted_text = pytesseract.image_to_string(Image.open(image_file))

            # Get all harmful ingredients from the database
            harmful_ingredients = HarmfulIngredient.objects.all()
            matched_ingredients = []

            # Check for matches in the extracted text
            for ingredient in harmful_ingredients:
                if ingredient.name.lower() in extracted_text.lower():
                    matched_ingredients.append({'name': ingredient.name, 'description': ingredient.description})

            # Return the matched ingredients as a JSON response
            return JsonResponse({'matched_ingredients': matched_ingredients})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

        finally:
            # Delete the file after processing
            if default_storage.exists(file_path):
                default_storage.delete(file_path)

    # If the request method is GET, render the upload form
    return render(request, 'index.html')
def About(request):
    return render(request, 'About.html')
def Contact(request):
    return render(request, 'Contact.html')
def Home(request):
    return render (request, 'Home.html')
def Ingredient(request):
    return render (request, 'Ingredient.html')

from django.shortcuts import render, HttpResponse
from PIL import Image
import pytesseract as pyt
from .models import *

def index(request):
    pyt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    if request.method == 'POST':
        try:
            image = request.FILES['image']
        except KeyError:
            return render(request, 'test.html', {'error': 'No image uploaded'})
        
        try:
            img = Image.open(image)
        except IOError:
            return render(request, 'test.html', {'error': 'Invalid image file'})
        
        try:
            text = pyt.image_to_string(img)
        except pyt.TesseractError:
            return render(request, 'test.html', {'error': 'Error occurred while processing the image'})
        
        try:
            item = request.POST.get('product_type')
        except KeyError:
            return render(request, 'test.html', {'error': 'No product type selected'})
        
        try:
            product = product_type.objects.get(product_name=item)  # Fetch the product that matches the name
        except product_type.DoesNotExist:
            return render(request, 'test.html', {'error': 'No data found for the selected product type'})
        
        # Split the text into phrases or keywords separated by commas
        try:
            phrases = [phrase.strip() for phrase in text.split(',')]
        except AttributeError:
            return render(request, 'test.html', {'error': 'Error occurred while processing the text'})
        
        # Match phrases with the models in your Django project
        matches = []
        try:
            for phrase in phrases:
                phrase_lower = phrase.lower()
                for obj in Harmful_Ingredients.objects.all():
                    if phrase_lower in obj.ingredient.lower():
                        matches.append(obj)
        except Exception as e:
            return render(request, 'test.html', {'error': str(e)})
        
        if not matches:
            message = "Product Safe to Eat!"
        else:
            message = None

        return render(request, 'test.html', {'text': text, 'matches': matches, 'product': product, 'message': message})
    return render(request, 'test.html')