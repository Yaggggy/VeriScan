import cv2
import pytesseract
import numpy as np
import re
from PIL import Image

# ✅ Set Tesseract path (Ensure it's installed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image_path):
    """Apply grayscale, thresholding, and denoising for better OCR results."""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # ✅ Apply adaptive thresholding to remove noise
    image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    
    # ✅ Denoise the image
    image = cv2.fastNlMeansDenoising(image, h=30)

    # ✅ Save temporary processed image
    processed_path = "backend/photos/processed_temp.jpg"
    cv2.imwrite(processed_path, image)

    return processed_path

def extract_aadhaar_details(image_path):
    """Extract Aadhaar details using OCR and regex."""
    processed_image_path = preprocess_image(image_path)
    
    # ✅ Run OCR on the preprocessed image
    text = pytesseract.image_to_string(Image.open(processed_image_path))

    # ✅ Extract Aadhaar number (12-digit pattern)
    aadhaar_match = re.search(r"\b\d{4}\s\d{4}\s\d{4}\b", text)
    aadhaar_number = aadhaar_match.group() if aadhaar_match else "Not Found"

    # ✅ Extract Name (Assume first uppercase word after "Name" or similar keywords)
    name_match = re.search(r"(?i)(name|नाम)[:\s]*([A-Z][a-z]+\s[A-Z][a-z]+)", text)
    name = name_match.group(2) if name_match else "Not Found"

    # ✅ Extract Date of Birth (Format: DD/MM/YYYY)
    dob_match = re.search(r"\b\d{2}/\d{2}/\d{4}\b", text)
    dob = dob_match.group() if dob_match else "Not Found"

    # ✅ Extract Address (Assume after "Address" or similar keywords)
    address_match = re.search(r"(?i)(address|पता)[:\s]*([\w\s,]+)", text)
    address = address_match.group(2) if address_match else "Not Found"

    return {
        "name": name,
        "aadhaar_number": aadhaar_number,
        "dob": dob,
        "address": address
    }
