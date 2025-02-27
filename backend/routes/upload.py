from flask import Blueprint, request, jsonify, current_app
from flask_cors import cross_origin
import os
from backend.extensions import db
from backend.models.user import User
from backend.services.ocr_extraction import extract_aadhaar_number

upload_blueprint = Blueprint("upload", __name__)

# ✅ Allow ONLY "POST" requests
@upload_blueprint.route("/upload", methods=["POST"])
@cross_origin(origins="http://localhost:3000")
def upload_file():
    try:
        print("📌 Request received!")

        # ✅ Check if the file is in the request
        if "file" not in request.files:
            print("❌ No file found in request")
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]
        if file.filename == "":
            print("❌ No file selected")
            return jsonify({"error": "No selected file"}), 400

        filename = file.filename
        file_path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)

        # ✅ Ensure Upload Folder Exists
        if not os.path.exists(current_app.config["UPLOAD_FOLDER"]):
            os.makedirs(current_app.config["UPLOAD_FOLDER"])

        file.save(file_path)
        print(f"✅ File uploaded successfully: {file_path}")

        # ✅ Extract Aadhaar number
        extracted_data = extract_aadhaar_number(file_path)
        aadhaar_number = extracted_data.get("aadhaar_number", "Not Found")

        if aadhaar_number == "Not Found":
            print("❌ OCR failed to extract Aadhaar number")
            return jsonify({"error": "OCR failed to extract Aadhaar number"}), 500

        # ✅ Check if Aadhaar number already exists in DB
        existing_user = User.query.filter_by(aadhaar_number=aadhaar_number).first()
        if existing_user:
            print("❌ Aadhaar number already exists in database")
            return jsonify({"error": "Aadhaar number already registered"}), 400

        # ✅ Store only Aadhaar number in the database
        new_user = User(aadhaar_number=aadhaar_number, photo_path=file_path)
        db.session.add(new_user)
        db.session.commit()

        print(f"✅ Aadhaar Number Stored: {aadhaar_number}")

        return jsonify({"message": "Upload successful!", "aadhaar_number": aadhaar_number}), 201

    except Exception as e:
        print(f"❌ Server Error: {e}")  # ✅ Print exact error in Flask console
        return jsonify({"error": f"Server error: {str(e)}"}), 500
