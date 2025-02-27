import cv2
import pytesseract
import re
import numpy as np
from PIL import Image

# Function to preprocess image
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to enhance contrast
    processed = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY, 11, 2)
    
    return processed

# Function to extract Aadhaar details using OCR
def extract_aadhaar_details(image_path):
    processed_image = preprocess_image(image_path)

    # Convert OpenCV image to PIL image for better OCR results
    pil_image = Image.fromarray(processed_image)

    # Use pytesseract to extract text
    raw_text = pytesseract.image_to_string(pil_image)

    # Use regex to extract Aadhaar details
    name_match = re.search(r"([A-Z][a-z]+\s[A-Z][a-z]+)", raw_text)
    aadhaar_match = re.search(r"\d{4}\s\d{4}\s\d{4}", raw_text)
    dob_match = re.search(r"(\d{2}/\d{2}/\d{4})", raw_text)
    address_match = re.search(r"Address:(.*)", raw_text, re.DOTALL)

    aadhaar_data = {
        "name": name_match.group(0) if name_match else "Not Found",
        "aadhaar_number": aadhaar_match.group(0) if aadhaar_match else "Not Found",
        "dob": dob_match.group(0) if dob_match else "Not Found",
        "address": address_match.group(1).strip() if address_match else "Not Found",
    }

    return aadhaar_data
