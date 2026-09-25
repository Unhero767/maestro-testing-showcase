import pytest
from fastapi.testclient import TestClient
from src.main.ingress.api import app

client = TestClient(app)

def test_crystallize_scar_endpoint():
    payload = {
        "identifier": "Test-Scar-Omega",
        "spectral_frequency": "Gold-Joy",
        "contradiction_vector": {"status": "resolved"},
        "intensity": 0.92
    }
    response = client.post("/scars/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["status"] == "crystallized"
    assert data["identifier"] == "test-scar-omega"

def test_telemetry_intensity_endpoint():
    response = client.get("/telemetry/intensity?voltages=1.0,0.8,0.5")
    assert response.status_code == 200
    data = response.json()
    assert data["voltages"] == [1.0, 0.8, 0.5]
    assert "consciousness_intensity_dphi_dt" in data

def test_telemetry_intensity_invalid_format():
    response = client.get("/telemetry/intensity?voltages=invalid,data")
    assert response.status_code == 400
    assert "Invalid voltage format" in response.json()["detail"]
