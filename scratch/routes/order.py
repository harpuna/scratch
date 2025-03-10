from flask_smorest import Blueprint
from models.error import ResourceNotFoundError
from models.order import Order
from schemas.customer import CustomerSchema
from schemas.order import OrderSchema

order_bp = Blueprint("Order", __name__, url_prefix="/api")


@order_bp.route("/orders", methods=["GET"])
@order_bp.response(200, OrderSchema(many=True))
def get_orders():
    orders = Order.all()
    return orders


@order_bp.route("/orders/<order_id>", methods=["GET"])
@order_bp.response(200, OrderSchema)
def get_order(order_id):
    order = Order.select(order_id)
    if order is None:
        raise ResourceNotFoundError(order_id)
    return order


@order_bp.route("/orders", methods=["POST"])
@order_bp.arguments(CustomerSchema)
@order_bp.response(201, OrderSchema)
def add_order(request: OrderSchema):
    new_order = Order.insert(request)
    return new_order
