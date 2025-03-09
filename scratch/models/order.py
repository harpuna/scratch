from app import db
from models import Base


class Order(Base):
    """
    See database scripts folder for specific DDL statements
    """

    __tablename__ = "order"

    id = db.Column(
        "order_id",
        db.Text,
        server_default=db.func.concat("order_id_", db.func.uuid_generate_v4()),
        primary_key=True,
    )
    total_amount_in_cents = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    # Many-to-one relationship with Customer, lazy-loaded
    customer_id = db.Column(
        db.Text, db.ForeignKey("customer.customer_id"), nullable=False
    )
    customer = db.relationship("Customer", back_populates="orders")
