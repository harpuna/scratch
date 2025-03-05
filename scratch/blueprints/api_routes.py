from flask_smorest import Blueprint
from flask import jsonify, request
from models.customer import Customer
from app import db

api_bp = Blueprint("api_bp", __name__, url_prefix="/api")

@api_bp.route("/test", methods=["GET"])
def test_api():
    return jsonify({"message": "Hello from API!"})


@api_bp.route("/customers", methods=["GET"])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{"id": customer.id, "name": customer.name, "email": customer.email} for customer in customers])

@api_bp.route("/customer/<customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if customer is None:
        return jsonify({"message": "Customer not found"}), 404
    return jsonify(customer.to_dict())



@api_bp.route("/customers", methods=["POST"])
def add_customer():
    data = request.json
    new_customer = Customer(name=data["name"], email=data["email"])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({"message": "Customer added successfully!"}), 201

@api_bp.route("/customers", methods=["PUT"])
def update_customer():
    data = request.json
    customer = Customer.query.filter_by(id=data["id"]).first()
    customer.name = data["name"]
    db.session.commit()
    return jsonify({"message": "Customer updated successfully!"})

@api_bp.route("/customers", methods=["DELETE"])
def delete_customer():
    customer = Customer.query.filter_by(id=request.json["id"]).first()
    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message": "Customer deleted successfully!"})


