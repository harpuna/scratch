from flask_smorest import Blueprint
from models.application import Application
from schemas.application import ApplicationSchema
from services.jsonplaceholder import calculate_term_and_rate
from utils.calculator import calculate_monthly_payment

application_bp = Blueprint("Application", __name__, url_prefix="/api")


@application_bp.route("/applications", methods=["POST"])
@application_bp.arguments(ApplicationSchema)
@application_bp.response(201, ApplicationSchema)
def add_application(request: Application):
    terms, rate = calculate_term_and_rate(request["total_amount_in_cents"])
    request["interest_rate_percent"] = rate
    request["term_months"] = terms
    if terms and rate:
        monthly_payment_in_cents = calculate_monthly_payment(
            request["total_amount_in_cents"], rate / 100.0, terms
        )
        request["monthly_payment_in_cents"] = int(monthly_payment_in_cents)

    new_application = Application.insert(request)
    return new_application
