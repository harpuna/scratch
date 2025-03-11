def test_add_application(app, mock_db_application, mock_application_dict):
    with app.test_client() as client:
        response = client.post("/api/applications", json=mock_application_dict)
    assert response.status_code == 201
    assert response.json == mock_application_dict
