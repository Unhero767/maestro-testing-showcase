"""Core engine module."""


class CoreEngine:
    def __init__(self, version: str = "1.0.0"):
        self.version = version

    def execute(self) -> str:
        return f"CoreEngine executing at version {self.version}"
