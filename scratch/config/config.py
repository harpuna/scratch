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
    OPENAPI_VERSION = "3.0.2"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", None)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    VERBOSE_LOGGING = os.getenv("VERBOSE_LOGGING", "False").lower() == "true"
