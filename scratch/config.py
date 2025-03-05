import os

class Config:
    API_TITLE = "My Flask API"  # <-- REQUIRED
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.2"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://flask_user:flask_password@localhost/flask_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

