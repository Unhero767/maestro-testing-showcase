from src.main.core.base import BaseCore


def test_base_core_init():
    core = BaseCore("TestProject")
    assert core.name == "TestProject"
    assert "TestProject" in core.get_info()
