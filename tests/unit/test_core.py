from src.main.core.engine import CoreEngine


def test_core_engine_execution():
    engine = CoreEngine("2.0.0")
    assert engine.version == "2.0.0"
    assert "2.0.0" in engine.execute()
