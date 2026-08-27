from fastapi.testclient import TestClient

from src.app.main import app


client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == (
        "GenAI Learning API"
    )

    assert data["environment"] == (
        "development"
    )


def test_process():

    response = client.post(
        "/process",
        json={
            "message": "Learn GenAI"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["result"] == (
        "Processed message: Learn GenAI"
    )