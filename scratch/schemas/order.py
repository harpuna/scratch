from marshmallow import EXCLUDE, Schema, fields, validate
from extensions import ma
from models.customer import Customer


class OrderSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Str(required=True, dump_only=True)
    customer_id = fields.Str(required=True)
    total_amount_in_cents = fields.Integer(required=True)
    description = fields.Str(required=True)

# class CustomerWithPostsSchema(CustomerSchema):
#     post = fields.Dict()
#     # post = fields.Dict(keys=fields.Str(), values=fields.Nested(CustomerSchema))
#
# class CustomerAutoSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Customer
#
# class CustomerPatchRequestSchema(CustomerSchema):
#     class Meta:
#         unknown = EXCLUDE
#
#     id = fields.Str()#required=True, dump_only=True)
#     name = fields.Str()#required=True)
#     email = fields.Str()#required=True)
