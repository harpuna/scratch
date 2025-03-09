def test_get_all_orders(app, mock_db_all_orders):
    with app.test_client() as client:
        response = client.get("/api/orders")

    assert response.status_code == 200
    assert len(response.json) > 0
    assert response.json[0]["id"] == "order_1"


def test_get_order_by_id(app, mock_db_order):
    with app.test_client() as client:
        response = client.get("/api/orders/order_123")

    assert response.status_code == 200
    assert response.json == {
        "customer_id": "customer_3",
        "description": "test order",
        "id": "order_2",
        "total_amount_in_cents": 1488,
    }
