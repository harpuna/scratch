from flask import render_template, request
from flask_smorest import Blueprint
from models import Customer
from schemas.customer import CustomerSchema
from services.jsonplaceholder import get_random_dog_href, get_word_of_the_day

web_bp = Blueprint(
    "Web Pages", __name__, template_folder="../templates", url_prefix="/web"
)


@web_bp.route("/test")
def test():
    schema = CustomerSchema()
    customers = Customer.query.all()

    return render_template(
        template_name_or_list="test.html",
        title="All Customers",
        customers=customers,
        schema=schema,
    )


@web_bp.route("/")
def home():
    schema = CustomerSchema()

    return render_template(
        template_name_or_list="index.html",
        title="Scratch!!",
        dog_url=get_random_dog_href(),
        schema=schema,
    )


@web_bp.route("/customer")
def customer_by_id():
    customer_id = request.args.get("id")
    cust = Customer.select(customer_id)
    schema = CustomerSchema()
    return render_template(
        template_name_or_list="customer.html",
        title="One Customer",
        customer=cust,
        schema=schema,
    )


@web_bp.route("/customer_created")
def customer_created():
    customer_id = request.args.get("id")
    cust = Customer.select(customer_id)
    schema = CustomerSchema()
    return render_template(
        template_name_or_list="customer_created.html",
        title="Customer Created",
        customer=cust,
        created_at=cust.created_at.strftime("%b %d, %Y"),
        word_of_the_day=get_word_of_the_day().upper(),
        schema=schema,
    )


@web_bp.route("/customer/<customer_id>")
def customer(customer_id):
    schema = CustomerSchema()
    return render_template(
        template_name_or_list="index.html", title="Customer", schema=schema
    )


@web_bp.route("/customer_new")
def customer_new():
    schema = CustomerSchema()
    return render_template(
        template_name_or_list="customer_new.html", title="New Customer", schema=schema
    )


@web_bp.route("/customer_list")
def customer_list():
    schema = CustomerSchema()
    customers = Customer.query.all()

    return render_template(
        template_name_or_list="customer_list.html",
        title="All Customers",
        customers=customers,
        schema=schema,
    )
