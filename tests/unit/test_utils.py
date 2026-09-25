from src.main.utils.helpers import sanitize_payload


def test_sanitize_payload():
    raw = "  HELLOWORLD  "
    assert sanitize_payload(raw) == "helloworld"
