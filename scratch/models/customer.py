from app import db
from models import Base


class Customer(Base):
    """
    create table public.customer
    (
        customer_id text
            default concat('customer_', replace((uuid_generate_v4())::text, '-'::text, ''::text))
            not null
            primary key,
        name        text not null,
        email       text not null,
        note        text,
        created_at  timestamp default now() not null,
        updated_at  timestamp default now() not null
    );
    """

    __tablename__ = "customer"

    id = db.Column(
        "customer_id",
        db.Text,
        server_default=db.func.concat(
            "customer_id_", db.func.uuid_generate_v4()
        ),
        primary_key=True,
    )
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    note = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Customer {self.name}>"
