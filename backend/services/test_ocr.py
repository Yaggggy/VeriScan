import pytesseract
import cv2
from PIL import Image
import numpy as np

# ✅ Set Tesseract Path (Modify if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ✅ Aadhaar Image Path (Update if needed)
image_path = "C:\Users\yagya\OneDrive\Desktop\VeriScan\photos\aadhaar.png"

# ✅ Load Image
image = cv2.imread(image_path)

# ✅ Convert to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ✅ Apply Thresholding
processed = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY, 11, 2)

# ✅ Convert to PIL Image
pil_image = Image.fromarray(processed)

# ✅ Extract Text
text = pytesseract.image_to_string(pil_image)

print("\n📝 Extracted Aadhaar Text:\n")
print(text)
