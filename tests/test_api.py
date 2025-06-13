from types import SimpleNamespace

import pytest
from fastapi.testclient import TestClient

from backend.main import app, get_client

class DummyCompletions:
    async def create(self, model: str, messages):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content="hi"))])

class DummyChat:
    def __init__(self):
        self.completions = DummyCompletions()

class DummyClient:
    def __init__(self):
        self.chat = DummyChat()

@pytest.fixture(autouse=True)
def override_client():
    app.dependency_overrides[get_client] = lambda: DummyClient()
    yield
    app.dependency_overrides.clear()

def test_chat_endpoint():
    client = TestClient(app)
    resp = client.post("/api/chat", json={"message": "Hello"})
    assert resp.status_code == 200
    assert resp.json() == {"response": "hi"}
