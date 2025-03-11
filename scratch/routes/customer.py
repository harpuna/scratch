from app import logger
from flask_smorest import Blueprint
from models.customer import Customer
from models.error import CustomerNotFound
from schemas.customer import (
    CustomerPatchRequestSchema,
    CustomerPostResponseSchema,
    CustomerSchema,
    CustomerWithPostsSchema,
)
from services.jsonplaceholder import get_post, get_post_comments

customer_bp = Blueprint("Customer", __name__, url_prefix="/api")


@customer_bp.route("/customers", methods=["GET"])
@customer_bp.response(200, CustomerSchema(many=True))
def get_customers():
    customers = Customer.query.all()
    logger().bind(all_customers_count=len(customers))
    return customers


@customer_bp.route("/customers/<customer_id>", methods=["GET"])
@customer_bp.response(200, CustomerSchema)
def get_customer(customer_id):
    logger().bind(customer_id=customer_id)
    customer = Customer.select(customer_id)
    if customer is None:
        raise CustomerNotFound(customer_id)
    return customer


@customer_bp.route("/customers/<customer_id>/posts/<post_id>", methods=["GET"])
@customer_bp.response(200, CustomerWithPostsSchema)
def get_customer_with_posts(customer_id, post_id):
    post = get_post(post_id)
    comments = get_post_comments(post_id)
    post["comments"] = comments

    customer = Customer.select(customer_id)
    if customer is None:
        return None, 404
    resp = {**customer.__dict__}
    resp["post"] = post
    return resp


@customer_bp.route("/customers", methods=["POST"])
@customer_bp.arguments(CustomerSchema)
@customer_bp.response(201, CustomerPostResponseSchema)
def add_customer(request: Customer):
    if request["name"] == "xxx":
        return {"errors": ["xxx is not an allowed name", "Invalid name"]}, 400
    new_customer = Customer.insert(request)
    return new_customer


@customer_bp.route("/customers/<customer_id>", methods=["PATCH"])
@customer_bp.arguments(CustomerPatchRequestSchema)
@customer_bp.response(200, CustomerSchema)
def update_customer(request: Customer, customer_id):
    updated_customer = Customer.update(customer_id, request)
    return updated_customer


@customer_bp.route("/customers/<customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    customer = Customer.delete(customer_id)
    if not customer:
        return {}, 404
    return {}, 204


# @customer_bp.route("/customers/find", methods=["GET"])
# def find_customer(customer_id):
#     data = request.json
#     customer = Customer.query.filter_by(id=data["id"]).first()
#     customer.name = data["name"]
#     db.session.commit()
#     return jsonify({"message": "Customer updated successfully!"})
