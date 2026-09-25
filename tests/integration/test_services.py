from src.main.services.adapter import DataAdapter

def test_adapter_connection():
    adapter = DataAdapter("sqlite:///:memory:")
    assert adapter.connect() is True
