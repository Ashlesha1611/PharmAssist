import os
import io
import json
import cv2
import numpy as np
from google.cloud import vision
from rapidfuzz import process  # Improved fuzzy matching

# Set up authentication (replace with your actual JSON key file)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "pharmacists-assistant-your key.json"

# Load medicine names from a JSON file
with open("medicines.json", "r") as file:
    medicine_data = json.load(file)

medicine_list = medicine_data["medicines"]  # Extract the list of medicine names

def preprocess_image(image_path):
    """Enhance image for better OCR results."""
    #print(f"Trying to read: {image_path}")
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        print(f"⚠️ Error: Couldn't read image {image_path}")

    
    image = cv2.resize(image, (800, 800))  # Resize for consistency
    image = cv2.GaussianBlur(image, (5,5), 0)  # Reduce noise
    _, image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # Binarization
    processed_path = os.path.join("processed_images", os.path.basename(image_path))

    cv2.imwrite(processed_path, image)
    return processed_path  # Return the new image path

def extract_text_from_image(image_path):
    """Extracts text from an image using Google Vision API."""
    client = vision.ImageAnnotatorClient()

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
        image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if not texts:
        return "⚠️ No text detected in the image."

    extracted_text = texts[0].description  # Full extracted text
    return extracted_text

def extract_medicine_names(ocr_text):
    """Extract only medicine names using fuzzy matching."""
    extracted_medicines = []
    words = ocr_text.split()
    
    for word in words:
        match, score, _ = process.extractOne(word, medicine_list)  # Using RapidFuzz
        if score > 90:  # 90% match confidence
            extracted_medicines.append(match)
    
    return list(set(extracted_medicines))  # Remove duplicates

def batch_process_images(image_paths):
    """Batch process multiple prescription images."""
    results = {}
    for image_path in image_paths:
        #print(os.path.getsize(image_path))
        #print(os.path.exists(image_path))
        processed_image_path = preprocess_image(image_path)  # Preprocess image before OCR
        extracted_text = extract_text_from_image(processed_image_path)
        medicines = extract_medicine_names(extracted_text)
        results[image_path] = {
            "extracted_text": extracted_text,
            "medicines": medicines
        }
    
    return results

# Example: Process multiple images in a folder
image_folder = "test_images/"  # Folder containing images
image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]

# Run batch processing
output_results = batch_process_images(image_files)

# Save results to JSON file
with open("output_medicines.json", "w") as json_file:
    json.dump(output_results, json_file, indent=4)

print("\n✅ Batch processing complete. Extracted medicines saved to output_medicines.json")
