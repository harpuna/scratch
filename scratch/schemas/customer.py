from extensions import ma
from marshmallow import EXCLUDE, Schema, fields, validate
from models.customer import Customer
from schemas.order import OrderSchema


class CustomerSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Str(required=True, dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=2, max=50))
    email = fields.Email(required=True)
    note = fields.Str(required=False)
    orders = ma.Nested(OrderSchema, many=True)


class CustomerWithPostsSchema(CustomerSchema):
    post = fields.Dict()


class CustomerAutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer


class CustomerPatchRequestSchema(CustomerSchema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Str()
    name = fields.Str()
    email = fields.Str()


class CustomerPostResponseSchema(CustomerSchema):
    errors = fields.List(fields.String(), required=False)
