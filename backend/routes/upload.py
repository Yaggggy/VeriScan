from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
import os
from backend.extensions import db
from backend.models.user import User
from backend.services.ocr_extraction import extract_aadhaar_details

upload_blueprint = Blueprint("upload", __name__)

@upload_blueprint.route("/upload", methods=["POST"])
@cross_origin(origins="http://localhost:3000")
def upload_file():
    try:
        print("📌 Request received!")  # ✅ Debugging log

        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        filename = file.filename
        file_path = os.path.join("backend/photos", filename)
        file.save(file_path)

        print(f"✅ File uploaded successfully: {file_path}")  # ✅ Debugging

        # ✅ Perform Aadhaar OCR extraction
        extracted_data = extract_aadhaar_details(file_path)
        print(f"✅ Extracted Data: {extracted_data}")  # ✅ Debugging

        return jsonify({"message": "Upload successful!", "data": extracted_data}), 201

    except Exception as e:
        print(f"❌ Server Error: {e}")  # ✅ Print exact error in Flask console
        return jsonify({"error": f"Server error: {str(e)}"}), 500
