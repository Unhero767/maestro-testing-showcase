from src.main.core.buffer import StreamBuffer


def test_stream_buffer_push_and_flush():
    buffer = StreamBuffer(capacity=3)
    buffer.push("data_1")
    buffer.push("data_2")
    
    items = buffer.flush()
    assert items == ["data_1", "data_2"]
    assert len(buffer.buffer) == 0
