"""Data adapter service module."""


class DataAdapter:
    def __init__(self, endpoint: str = "localhost"):
        self.endpoint = endpoint

    def fetch_data(self) -> dict:
        return {"status": "connected", "endpoint": self.endpoint}
