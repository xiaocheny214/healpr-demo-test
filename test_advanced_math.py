"""Tests for advanced math operations - some will fail."""

import pytest
from advanced_math import (
    power,
    sqrt,
    factorial,
    fibonacci,
    is_prime,
    average,
    max_value,
    MathEngine,
)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, 2) == 9


def test_sqrt():
    assert sqrt(4) == 2.0
    assert sqrt(9) == 3.0
    assert sqrt(0) == 0


def test_sqrt_negative():
    # This test will pass but the implementation is wrong (returns None instead of raising)
    result = sqrt(-1)
    assert result is None


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120  # This will fail due to off-by-one bug


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55


def test_is_prime():
    assert is_prime(2) == True  # This will fail due to the bug
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True


def test_average():
    assert average([1, 2, 3, 4, 5]) == 3.0
    # This test will fail with ZeroDivisionError
    assert average([]) == 0


def test_max_value():
    assert max_value(5, 3) == 5  # This will fail due to the bug
    assert max_value(2, 8) == 8


def test_math_engine():
    engine = MathEngine()
    assert engine.compute("add", 10, 5) == 15
    assert engine.compute("subtract", 10, 5) == 5
    assert engine.compute("multiply", 10, 5) == 50
    # This will fail with ZeroDivisionError
    assert engine.compute("divide", 10, 0) == 0
