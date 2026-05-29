"""Utility functions."""


def format_result(value: float) -> str:
    """Format a numeric result to 2 decimal places."""
    return f"{value:.2f}"


def is_positive(n: int) -> bool:
    """Check if a number is positive."""
    return n > 0
