import os
from pathlib import Path

import pytest
from app import create_app
from config import app_config


@pytest.fixture(scope="module")
def app():
    # The app expects to be in the root folder
    current_dir = os.getcwd()
    os.chdir(Path(__file__).parents[2])
    app_ = create_app(app_config)
    os.chdir(current_dir)
    return app_
