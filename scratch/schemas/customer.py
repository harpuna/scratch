from marshmallow import EXCLUDE, Schema, fields, validate
from extensions import ma
from models.customer import Customer


class CustomerSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Str(required=True, dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    note = fields.Str(required=False)  #, dump_default=None, load_default=None)

class CustomerAutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer

class CustomerPatchRequestSchema(CustomerSchema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Str()#required=True, dump_only=True)
    name = fields.Str()#required=True)
    email = fields.Str()#required=True)
