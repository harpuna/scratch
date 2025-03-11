def test_get_all_customers(app, mock_db_customer):
    with app.test_client() as client:
        response = client.get("/api/customers")

    assert response.status_code == 200
    assert len(response.json) > 0
    assert response.json[0]["id"] == "customer_1"


def test_get_customer_by_id(app, mock_db_customer, mock_customer_dict, mock_order_dict):
    with app.test_client() as client:
        response = client.get("/api/customers/customer_123")

    assert response.status_code == 200
    assert response.json == {
        **mock_customer_dict,
        **{"orders": [mock_order_dict, mock_order_dict]},
    }


def test_add_customer(app, mock_db_customer, mock_customer_dict):
    with app.test_client() as client:
        response = client.post("/api/customers", json=mock_customer_dict)

    assert response.status_code == 201
    assert response.json == mock_customer_dict


def test_add_customer_invalid_name(app, mock_db_customer, mock_customer_dict):
    with app.test_client() as client:
        response = client.post(
            "/api/customers", json={**mock_customer_dict, **{"name": "xxx"}}
        )

    assert response.status_code == 400
    assert response.json == {"errors": ["xxx is not an allowed name", "Invalid name"]}
