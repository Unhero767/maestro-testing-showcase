from src.main.utils.helpers import sanitize_payload

def test_sanitize_payload_formatting():
    assert sanitize_payload("  TEST_PAYLOAD  ") == "test_payload"
