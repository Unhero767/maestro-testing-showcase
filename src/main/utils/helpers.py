"""Utility helper functions."""


def sanitize_payload(payload: str) -> str:
    """Clean up and sanitize incoming string payloads."""
    return payload.strip().lower()
