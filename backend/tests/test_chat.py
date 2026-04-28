from fastapi.testclient import TestClient
from app.main import app
from app.routes import chat

client = TestClient(app)


def test_chat_success(monkeypatch):
    def fake_ai_answer(question, context):
        return "Mock AI answer for insurance question."

    monkeypatch.setattr(chat, "generate_ai_answer", fake_ai_answer)

    response = client.post(
        "/api/chat/",
        json={"question": "How do I submit a car accident claim?"}
    )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data
    assert "sources" in data
    assert isinstance(data["sources"], list)