from flask_smorest import Blueprint
from flask import render_template

from schemas.customer import CustomerSchema

web_bp = Blueprint("web_bp", __name__, template_folder="../templates", url_prefix="/web")

@web_bp.route("/")
def home():
    schema = CustomerSchema()
    return render_template("index.html", title="Scratch Web App!!", schema=schema)

@web_bp.route("/customer")
def customer():
    schema = CustomerSchema()
    return render_template("customer.html", title="Scratch Web App!!", schema=schema)

@web_bp.route("/customer/<customer_id>")
def customer(customer_id):
    schema = CustomerSchema()
    return render_template("index.html", title="Scratch Web App!!", schema=schema)

