from marshmallow import EXCLUDE, Schema, fields


class ApplicationSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Str(required=True, dump_only=True)
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)
    ssn = fields.Str(required=True)
    total_amount_in_cents = fields.Integer()
    interest_rate_percent = fields.Integer()
    term_months = fields.Integer()
    monthly_payment_in_cents = fields.Integer()
