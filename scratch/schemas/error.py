from extensions import ma
from marshmallow import Schema


class ScratchErrorSchema(Schema):
    code = ma.Integer(required=True)
    error_type = ma.String(required=True)
    message = ma.String(required=True)


class ResourceNotFoundSchema(ScratchErrorSchema):
    resource_id = ma.String(required=True)
