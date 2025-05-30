import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Valid sample with 63 values
valid_input = {
    "landmarks": [0.1] * 63
}

# Invalid sample with less than 63 values
invalid_input = {
    "landmarks": [0.1] * 10
}

def test_predict_valid_input():
    response = client.post("/predict", json=valid_input)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] in ["left", "right", "up", "down", "unknown"]

def test_predict_invalid_input():
    response = client.post("/predict", json=invalid_input)
    assert response.status_code == 400
    assert "Input landmarks length must be 63" in response.json()["detail"]
