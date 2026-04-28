from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_search_articles_success():
    response = client.get("/api/search/?q=claim")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_search_articles_missing_query():
    response = client.get("/api/search/")

    assert response.status_code == 422

def test_chat_validation_error():
    response = client.post(
        "/api/chat/",
        json={}
    )

    assert response.status_code == 422