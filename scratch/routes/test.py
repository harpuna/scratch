from flask import jsonify
from flask_smorest import Blueprint

test_bp = Blueprint("test", __name__, url_prefix="/test")

@test_bp.route("/data", methods=["GET"])
def get_data():
    return jsonify({"message": "Hello from Flask API!"})
