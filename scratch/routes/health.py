from flask_smorest import Blueprint

health_bp = Blueprint("health", __name__, url_prefix="/health")


@health_bp.route("", methods=["GET"])
def get_health():
    return {"status": "Healthy"}
