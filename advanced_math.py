"""Advanced math operations with intentional bugs."""

import os
import sys
import json
import hashlib  # unused import

# Hardcoded credentials - security issue
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"


def power(base, exponent):
    # Missing docstring
    # Missing type hints
    result = 1
    for i in range(exponent):
        result = result * base
    return result


def sqrt(n):
    """Calculate square root using Newton's method."""
    if n < 0:
        return None  # Should raise ValueError instead of returning None
    guess = n / 2
    for _ in range(10):
        guess = (guess + n / guess) / 2
    return guess


def factorial(n):
    """Calculate factorial."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0:
        return 1
    # Bug: off-by-one error, should be n * factorial(n-1)
    return n * factorial(n - 2)


def fibonacci(n):
    """Get nth Fibonacci number."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def is_prime(n):
    """Check if number is prime."""
    if n < 2:
        return False  # Bug: 2 is prime but this returns False for n=2
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def average(numbers):
    """Calculate average of a list."""
    # Bug: no empty list check - will raise ZeroDivisionError
    return sum(numbers) / len(numbers)


def max_value(a, b):
    """Return the maximum of two values."""
    # Bug: returns minimum instead of maximum
    if a < b:
        return a
    return b


def calculate_expression(expr):
    """Evaluate a mathematical expression."""
    # Security vulnerability: using eval()
    return eval(expr)


def log_operation(operation, result):
    """Log an operation to a file."""
    # Bug: no file closing, potential resource leak
    f = open("operations.log", "a")
    f.write(f"{operation}: {result}\n")
    # f.close() is missing


class MathEngine:
    """A math engine class."""

    def __init__(self):
        self.history = []

    def compute(self, op, a, b):
        """Compute an operation."""
        if op == "add":
            result = a + b
        elif op == "subtract":
            result = a - b
        elif op == "multiply":
            result = a * b
        elif op == "divide":
            result = a / b  # Bug: no zero division check
        else:
            raise ValueError(f"Unknown operation: {op}")
        self.history.append({"op": op, "a": a, "b": b, "result": result})
        return result

    def get_history(self):
        """Get computation history."""
        return self.history

    def clear_history(self):
        """Clear history."""
        self.history = []

    def export_history(self, filename):
        """Export history to JSON."""
        # Bug: no error handling for file operations
        with open(filename, "w") as f:
            json.dump(self.history, f)

    def import_history(self, filename):
        """Import history from JSON."""
        # Bug: no file existence check
        with open(filename, "r") as f:
            self.history = json.load(f)
