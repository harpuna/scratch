import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

env = os.getenv("ENVIRON", "dev")
basedir = os.path.dirname(Path(__file__).parent.parent)
load_dotenv(os.path.join(basedir, ".flaskenv"))
load_dotenv(os.path.join(basedir, f"conf/.{env}env"))


@dataclass
class Config(object):
    ENVIRON = os.getenv("ENVIRON", "dev")
    API_TITLE = os.getenv("API_TITLE", "Scratch Demo")
    API_VERSION = "v1"
    OPENAPI_VERSION = os.getenv("OPENAPI_VERSION")
    OPENAPI_URL_PREFIX = os.getenv("OPENAPI_URL_PREFIX")
    OPENAPI_SWAGGER_UI_PATH = os.getenv("OPENAPI_SWAGGER_UI_PATH")
    OPENAPI_SWAGGER_UI_URL = os.getenv("OPENAPI_SWAGGER_UI_URL")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", None)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    VERBOSE_LOGGING = os.getenv("VERBOSE_LOGGING", "False").lower() == "true"
