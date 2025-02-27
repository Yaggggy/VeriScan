import pytesseract
import cv2

# Set path to Tesseract OCR (change for Windows if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_aadhaar_details(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Run OCR
    extracted_text = pytesseract.image_to_string(gray)

    # Process text to find Aadhaar details
    details = {"name": "", "aadhaar_number": "", "dob": "", "address": ""}
    
    lines = extracted_text.split("\n")
    for line in lines:
        if "Name" in line:
            details["name"] = line.split(":")[-1].strip()
        if "DOB" in line or "Year of Birth" in line:
            details["dob"] = line.split(":")[-1].strip()
        if "Address" in line:
            details["address"] = line.split("Address")[-1].strip()
        if len(line.replace(" ", "")) == 12 and line.replace(" ", "").isdigit():
            details["aadhaar_number"] = line.strip()

    if details["aadhaar_number"]:
        return details
    else:
        return None
