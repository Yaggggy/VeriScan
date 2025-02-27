from flask import Blueprint, jsonify

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/test", methods=["GET"])
def test_route():
    return jsonify({"message": "User route is working!"}), 200
