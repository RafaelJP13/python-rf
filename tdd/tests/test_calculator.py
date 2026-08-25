# TDD - Test Driven Development

import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(10, 5) == 15

def test_subtract():
    assert subtract(5, 5) == 0
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(5, 10) == 50
    assert multiply(0.5, 10) == 5.0

def test_divide():
    assert divide(16, 8) == 2
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)