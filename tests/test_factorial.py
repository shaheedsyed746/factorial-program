
from app import factorial

def test_factorial_5():
    assert factorial(5) == 120

def test_factorial_4():
    assert factorial(4) == 24

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_negative_number():
    try:
        factorial(-5)
        assert False
    except ValueError:
        assert True
