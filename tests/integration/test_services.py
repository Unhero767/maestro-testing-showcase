from src.main.services.adapter import DataAdapter


def test_data_adapter_integration():
    adapter = DataAdapter("127.0.0.1")
    data = adapter.fetch_data()
    assert data["status"] == "connected"
    assert data["endpoint"] == "127.0.0.1"
