from src.train_actions import simple_function as sf


def test_simple_function():
    assert sf("x")
    assert not sf(int(1))
