from app import db
from models import Base


class Customer(Base):
    """
    See database scripts folder for specific DDL statements
    """

    __tablename__ = "customer"

    id = db.Column(
        "customer_id",
        db.Text,
        server_default=db.func.concat("customer_id_", db.func.uuid_generate_v4()),
        primary_key=True,
    )
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    note = db.Column(db.Text, nullable=True)

    # One-to-many relationship with Order, lazy-loaded
    orders = db.relationship(
        "Order", back_populates="customer", cascade="all, delete-orphan", lazy="joined"
    )
