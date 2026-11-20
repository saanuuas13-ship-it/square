from square import calculate_square

def test_positive():
    assert calculate_square(2) == 4

def test_negative():
    assert calculate_square(-4) == 16