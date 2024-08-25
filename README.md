# NutriScan
NutriScan project is a Django-based web application designed to help users scan and analyze the ingredients of daily life products like packaged food, drinks, and cosmetics. The key features of your project include:

**Scanning Ingredients:** Users can upload images of product labels, which are then processed using Optical Character Recognition (OCR) technology (specifically Tesseract) to extract text from the images.

**Identifying Harmful Chemicals:** The extracted ingredients are compared against a database of known ingredients. The app identifies potentially harmful chemicals in the scanned products and alerts the user about these ingredients.

**Interactive User Interface:** The app includes a dynamic UI with a full-background image, additional images in the corners that disappear when clicked, and interactive elements that enhance user engagement.

**Database Integration:** Django's models.py to manage a database that stores ingredients and their descriptions. The app matches extracted ingredients from scanned images with those listed in the database to provide users with detailed information about each ingredient, especially highlighting any harmful ones.

**Optimized Performance:** Here i'm  focused on optimizing the Django views to handle OCR processing efficiently, ensuring a smooth user experience even with potentially high computational demands.

Overall, nutriScan project aims to be a user-friendly tool for consumers to better understand the products we use daily, promoting informed choices by highlighting the presence of harmful chemicals.




