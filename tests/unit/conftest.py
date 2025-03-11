import pytest
from models import Customer, Order


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
