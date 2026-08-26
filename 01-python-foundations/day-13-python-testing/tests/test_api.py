from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Testing API"
    }


def test_create_user():

    response = client.post(
        "/users",
        json={
            "name": "Siddharth",
            "age": 25
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "User created"

    assert data["user"]["name"] == "Siddharth"

    assert data["user"]["age"] == 25


def test_invalid_user():

    response = client.post(
        "/users",
        json={
            "name": "A",
            "age": 10
        }
    )

    assert response.status_code == 422