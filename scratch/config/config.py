import os
from dataclasses import dataclass


@dataclass
class Config(object):
    API_TITLE = "Scratch Demo"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.2"
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://flask_user:flask_password@localhost/flask_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = "prod"
