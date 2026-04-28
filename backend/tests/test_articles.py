from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_articles():
    response = client.get("/api/articles/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_article_not_found():
    response = client.get("/api/articles/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Article not found"