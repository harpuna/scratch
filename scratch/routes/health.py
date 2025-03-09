from flask_smorest import Blueprint

test_bp = Blueprint("health", __name__, url_prefix="/health")


@test_bp.route("", methods=["GET"])
def get_health():
    return {"status": "Healthy"}
