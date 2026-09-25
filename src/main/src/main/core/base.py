"""Core module base functionality."""


class BaseCore:
    def __init__(self, name: str = "MaestroProject"):
        self.name = name

    def get_info(self) -> str:
        return f"Running core module for: {self.name}"
