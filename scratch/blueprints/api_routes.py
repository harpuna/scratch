from flask_smorest import Blueprint
from flask import jsonify
from models.customer import Customer
from schemas.customer import CustomerSchema, CustomerPatchRequestSchema

api_bp = Blueprint("api_bp", __name__, url_prefix="/api")

@api_bp.route("/test", methods=["GET"])
def test_api():
    return jsonify({"message": "Hello from API!"})


@api_bp.route("/customers", methods=["GET"])
@api_bp.response(200, CustomerSchema(many=True))
def get_customers():
    customers = Customer.query.all()
    return customers

@api_bp.route("/customers/<customer_id>", methods=["GET"])
@api_bp.response(200, CustomerSchema)
def get_customer(customer_id):
    customer = Customer.select(customer_id)
    if customer is None:
        return None, 404
    return customer


@api_bp.route("/customers", methods=["POST"])
@api_bp.arguments(CustomerSchema)
@api_bp.response(201, CustomerSchema)
def add_customer(request: Customer):
    new_customer = Customer.insert(request)
    # new_customer = Customer(name=request["name"], email=request["email"], note=request["note"])
    # db.session.add(new_customer)
    # db.session.commit()
    return new_customer

@api_bp.route("/customers/<customer_id>", methods=["PATCH"])
@api_bp.arguments(CustomerPatchRequestSchema)
@api_bp.response(200, CustomerSchema)
def update_customer(request: Customer, customer_id):
    updated_customer = Customer.update(customer_id, request)
    return updated_customer


@api_bp.route("/customers/<customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    customer = Customer.delete(customer_id)
    if not customer:
        return {}, 404
    return {}, 204


# @api_bp.route("/customers/find", methods=["GET"])
# def find_customer(customer_id):
#     data = request.json
#     customer = Customer.query.filter_by(id=data["id"]).first()
#     customer.name = data["name"]
#     db.session.commit()
#     return jsonify({"message": "Customer updated successfully!"})