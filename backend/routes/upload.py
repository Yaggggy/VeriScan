import os
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from backend.extensions import db
from backend.models.user import User
from backend.services.ocr_extraction import extract_aadhaar_details

upload_blueprint = Blueprint("upload", __name__)

UPLOAD_FOLDER = "backend/photos"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# ✅ Aadhaar Upload API
@upload_blueprint.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and "." in file.filename and file.filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS:
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        # ✅ Extract Aadhaar details using OCR
        aadhaar_data = extract_aadhaar_details(file_path)

        # ✅ Store in database
        new_user = User(
            name=aadhaar_data["name"],
            aadhaar_number=aadhaar_data["aadhaar_number"],
            dob=aadhaar_data["dob"],
            address=aadhaar_data["address"],
            photo_path=file_path,
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "Upload successful!", "data": aadhaar_data}), 200

    return jsonify({"error": "Invalid file format"}), 400
