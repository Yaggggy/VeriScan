from backend.services.ocr_extraction import extract_aadhaar_details

image_path = "C:\\Users\\yagya\\OneDrive\\Desktop\\VeriScan\\backend\\photos\\aadhaar.jpg"
aadhaar_data = extract_aadhaar_details(image_path)

print("Extracted Data:", aadhaar_data)
