from flask_smorest import Blueprint

health_bp = Blueprint("Health", __name__, url_prefix="/health")


@health_bp.route("", methods=["GET"])
def get_health():
    return {"status": "Healthy"}
