def test_invalid_id(flask_client):
    """If ID is not num should get validation error"""

    response = flask_client.get(f"/msg-scheduler?id=abcde")
    assert response.status_code == 400
    assert response.json == {"message": "id: Not a valid integer."}


def test_missing_POST_data(flask_client):
    """If call type is not valid should get validation error"""
    response = flask_client.post("/msg-scheduler")

    assert response.status_code == 400


