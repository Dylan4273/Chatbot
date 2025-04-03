from fastapi.testclient import TestClient
from main import app
import pytest

@pytest.fixture(name="api")
def api_fixture():
    api = TestClient(app)
    yield api

def test_root(api):
    response = api.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello! from chatbot"}