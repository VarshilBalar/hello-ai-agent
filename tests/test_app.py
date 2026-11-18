from hello_agent.app import calculate, greet


def test_greet():
    assert greet() == "HELLO"

def test_calculate():
    assert calculate() == 4

def test_calculate_type():
    assert isinstance(calculate(), int)