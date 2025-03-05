from app import db

class Customer(db.Model):
    __tablename__ = "customer"

    id = db.Column("customer_id", db.Text, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return f"<Customer {self.name}>"
