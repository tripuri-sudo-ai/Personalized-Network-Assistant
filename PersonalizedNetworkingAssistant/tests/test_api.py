import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_analyze_event():
    response = client.post(
        "/analyze-event",
        json={
            "event_description": "AI Healthcare Conference",
            "interests": "Machine Learning"
        }
    )

    assert response.status_code == 200
    assert "themes" in response.json()


def test_generate_conversation():
    response = client.post(
        "/generate-conversation",
        json={
            "topic": "Artificial Intelligence"
        }
    )

    assert response.status_code == 200
    assert "conversation" in response.json()


def test_fact_check():
    response = client.post(
        "/fact-check",
        json={
            "topic": "Artificial Intelligence"
        }
    )

    assert response.status_code == 200
    assert "summary" in response.json()