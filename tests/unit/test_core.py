from src.main.core.engine import CoreEngine

def test_engine_evaluation(sample_payload):
    engine = CoreEngine()
    assert engine.evaluate(sample_payload) is True
