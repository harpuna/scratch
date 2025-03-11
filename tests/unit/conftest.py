import pytest
from models import Customer, Order
from models.application import Application


@pytest.fixture
def mock_order_dict():
    return {
        "id": "order_1",
        "customer_id": "customer_1",
        "description": "test order",
        "total_amount_in_cents": 1995,
    }


@pytest.fixture
def mock_db_order(mocker, mock_order_dict):
    all_order_mock = mocker.patch("routes.order.Order.all")
    select_order_mock = mocker.patch("routes.order.Order.select")
    order = Order(**mock_order_dict)
    select_order_mock.return_value = order
    all_order_mock.return_value = [order, order]


@pytest.fixture
def mock_customer_dict():
    return {
        "email": "emily@gmail.com",
        "id": "customer_1",
        "name": "Emily Dickinson",
        "note": "famous poet",
        "orders": [],
    }


@pytest.fixture
def mock_db_customer(mocker, mock_customer_dict, mock_order_dict):
    customer_all_mock = mocker.patch("routes.customer.Customer.all")
    customer_select_mock = mocker.patch("routes.customer.Customer.select")
    new_customer_mock = mocker.patch("routes.customer.Customer.insert")

    order = Order(**mock_order_dict)
    customer_with_orders = Customer(**mock_customer_dict)
    customer_with_orders.orders = [order, order]

    customer_select_mock.return_value = customer_with_orders
    customer_all_mock.return_value = [customer_with_orders, customer_with_orders]

    customer_no_orders = Customer(**mock_customer_dict)
    new_customer_mock.return_value = customer_no_orders

    # return customer_select_mock


@pytest.fixture
def mock_application_dict():
    return {
        "address": "123 First St",
        "email": "jesse@ross.com",
        "id": "app_2cb04c5af18c4067ac6fbd2874275ad1",
        "interest_rate_percent": 10,
        "monthly_payment_in_cents": 36972,
        "name": "hello",
        "phone": "111223333",
        "ssn": "111223333",
        "term_months": 36,
        "total_amount_in_cents": 1000000,
    }


@pytest.fixture
def mock_db_application(mocker, mock_application_dict):
    new_application_mock = mocker.patch("routes.application.Application.insert")
    application = Application(**mock_application_dict)
    new_application_mock.return_value = application
