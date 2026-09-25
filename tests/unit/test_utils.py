from src.main.utils.helpers import sanitize_payload

def test_sanitize_payload(sample_payload):
    cleaned = sanitize_payload(sample_payload)
    assert "metadata" not in cleaned
    assert cleaned["id"] == 1
