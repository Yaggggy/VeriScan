import cv2
import pytesseract
import easyocr
import numpy as np
import re
from PIL import Image

# ✅ Set Tesseract Path (Ensure Tesseract is installed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ✅ Initialize EasyOCR Reader
reader = easyocr.Reader(["en"])  # Supports multiple languages if needed

def preprocess_image(image_path):
    """Enhance image quality for better OCR detection."""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # ✅ Apply Adaptive Thresholding to remove noise
    image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # ✅ Apply Denoising to reduce artifacts
    image = cv2.fastNlMeansDenoising(image, h=30)

    # ✅ Save the processed image for debugging
    processed_path = "backend/photos/processed_temp.jpg"
    cv2.imwrite(processed_path, image)

    return processed_path

def extract_text_tesseract(image_path):
    """Extract raw text from image using Tesseract OCR."""
    processed_image_path = preprocess_image(image_path)
    text = pytesseract.image_to_string(Image.open(processed_image_path), config="--psm 6")  # ✅ PSM 6 for structured text
    return text

def extract_aadhaar_number(image_path, use_easyocr=False):
    """Extract only the Aadhaar number using OCR."""
    
    # ✅ Use EasyOCR if specified, otherwise use Tesseract
    text = extract_text_tesseract(image_path)

    # ✅ Debugging: Print extracted text
    print("📌 Extracted OCR Text:\n", text)

    # ✅ Extract Aadhaar Number (Handles different formats)
    aadhaar_match = re.search(r"\b\d{4}[\s\-]?\d{4}[\s\-]?\d{4}\b", text)
    aadhaar_number = aadhaar_match.group().replace(" ", "").replace("-", "") if aadhaar_match else "Not Found"

    return {"aadhaar_number": aadhaar_number}
