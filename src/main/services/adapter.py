"""Interface and adapters for external services/databases."""

class DataAdapter:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def connect(self) -> bool:
        return len(self.connection_string) > 0
