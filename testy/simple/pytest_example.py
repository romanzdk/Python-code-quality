from testy.app import add

def test_add_positive_numbers():
    assert add(3, 4) == 7

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_positive_and_negative_number():
    assert add(-5, 5) == 0
