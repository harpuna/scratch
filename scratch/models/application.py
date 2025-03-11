from app import db
from models import Base


class Application(Base):

    __tablename__ = "application"

    id = db.Column(
        "application_id",
        db.Text,
        server_default=db.func.concat("app_", db.func.uuid_generate_v4()),
        primary_key=True,
    )
    name = db.Column(db.Text, nullable=False)
    address = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text, nullable=False)
    ssn = db.Column(db.Text, nullable=False)

    total_amount_in_cents = db.Column(db.Integer)
    interest_rate_percent = db.Column(db.Integer)
    term_months = db.Column(db.Integer)
    monthly_payment_in_cents = db.Column(db.Integer)
