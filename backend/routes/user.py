from flask import Blueprint, jsonify
from backend.extensions import db
from backend.models.user import User

user_blueprint = Blueprint("user", __name__)

# ✅ Fetch all registered Aadhaar users
@user_blueprint.route("/get_users", methods=["GET"])
def get_users():
    users = User.query.all()
    user_list = [
        {
            "id": user.id,
            "aadhaar_number": user.aadhaar_number,
            "photo_path": user.photo_path,
        }
        for user in users
    ]
    return jsonify(user_list)
