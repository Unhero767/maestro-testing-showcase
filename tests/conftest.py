import pytest

@pytest.fixture
def sample_payload():
    return {"id": 1, "status": "active", "metadata": None}
