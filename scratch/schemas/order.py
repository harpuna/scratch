from marshmallow import EXCLUDE, Schema, fields


class OrderSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Str(required=True, dump_only=True)
    customer_id = fields.Str(required=True)
    total_amount_in_cents = fields.Integer(required=True)
    description = fields.Str(required=True)
