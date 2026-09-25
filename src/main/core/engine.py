"""Core business logic engine."""

class CoreEngine:
    def __init__(self, name: str = "SmartEngine"):
        self.name = name
        self.active = True

    def evaluate(self, data: dict) -> bool:
        return self.active and bool(data)
