import os
from pathlib import Path

import pytest
from app import create_app
from config import app_config
from models import Order


@pytest.fixture(scope="module")
def app():
    # The app expects to be in the root folder
    current_dir = os.getcwd()
    os.chdir(Path(__file__).parents[2])
    app_ = create_app(app_config)
    os.chdir(current_dir)
    return app_


@pytest.fixture
def mock_db_order(mocker):
    order_mock = mocker.patch("routes.order.Order.select")
    order = Order(
        id="order_2",
        customer_id="customer_3",
        description="test order",
        total_amount_in_cents=1488,
    )
    order_mock.return_value = order
    return order_mock


@pytest.fixture
def mock_db_all_orders(mocker):
    order_mock = mocker.patch("routes.order.Order.all")
    order = Order(
        id="order_1",
        customer_id="customer_2",
        description="test order",
        total_amount_in_cents=1995,
    )
    order_mock.return_value = [order, order]
    return order_mock
