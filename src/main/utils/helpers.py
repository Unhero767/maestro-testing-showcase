"""Reusable utility helpers."""

def sanitize_payload(payload: dict) -> dict:
    return {k: v for k, v in payload.items() if v is not None}
