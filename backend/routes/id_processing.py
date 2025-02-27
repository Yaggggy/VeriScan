from flask import Blueprint, request, jsonify

id_blueprint = Blueprint("id_processing", __name__)

@id_blueprint.route("/", methods=["GET"])
def test_route():
    return jsonify({"message": "VeriScan backend is running!"}), 200
