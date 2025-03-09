from app import db
from models import Base


class Order(Base):
    """
    create table public.order
    (
        order_id text
            default concat('order_', replace((uuid_generate_v4())::text, '-'::text, ''::text))
            not null
            primary key,
        customer_id text references customer(customer_id),
        total_amount_in_cents   integer not null,
        description             text,
        created_at              timestamp default now() not null,
        updated_at              timestamp default now() not null
    );
    """

    __tablename__ = "order"

    id = db.Column(
        "order_id",
        db.Text,
        server_default=db.func.concat(
            "order_id_", db.func.uuid_generate_v4()
        ),
        primary_key=True,
    )
    total_amount_in_cents = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    customer_id = db.Column(db.Text, db.ForeignKey('customer.customer_id'), nullable=False)
    customer = db.relationship('Customer', back_populates='orders')

    def __repr__(self):
        return f"<Order {self.description}>"

    @classmethod
    def get_all(cls):
        import pprint
        print(f"\n\n---------model get_all----------------------------\n")

        return cls.query.all()