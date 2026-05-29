"""Tests that are themselves buggy or insufficient."""
import pytest
from data.processor import find_duplicates, fibonacci, process_batch


def test_find_duplicates():
    """Test with only simple case."""
    # Missing edge cases
    assert find_duplicates([1, 2, 3, 2, 1]) == [1, 2]
    # Not testing: empty list, no duplicates, all same


def test_fibonacci():
    """Test that will timeout."""
    # This will be very slow
    assert fibonacci(40) == 102334155


def test_process_batch():
    """Test with wrong expected value."""
    # Off-by-one not caught because test matches buggy behavior
    result = process_batch([1, 2, 3, 4, 5], batch_size=2)
    assert len(result) == 4  # Should be 5 but test matches bug


def test_always_passes():
    """Useless test."""
    assert True  # This test proves nothing


def test_with_assertion_message():
    """Test with assertion that never fails."""
    x = 5
    assert x > 0, "x should be positive"  # Trivial assertion

# No tests for edge cases, error conditions, or boundary values
# No tests for security-related functions
# No integration tests
