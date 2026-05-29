"""Data processor with performance and logic issues."""
import time
import threading

# Global mutable state - thread safety issue
shared_counter = 0
results_cache = {}

def find_duplicates(items: list) -> list:
    """Find duplicate items - O(n^2) performance issue."""
    duplicates = []
    # Nested loop instead of using a set - O(n^2)
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates


def process_batch(data: list, batch_size: int = 100) -> list:
    """Process data in batches - off-by-one error."""
    results = []
    # Off-by-one: misses last element
    for i in range(0, len(data) - 1, batch_size):
        batch = data[i:i + batch_size]
        results.extend([x * 2 for x in batch])
    return results


def fibonacci(n: int) -> int:
    """Calculate fibonacci - exponential time complexity."""
    # No memoization - O(2^n) time complexity
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def increment_counter(amount: int = 1):
    """Increment shared counter - race condition."""
    global shared_counter
    # Race condition: read-modify-write is not atomic
    temp = shared_counter
    time.sleep(0.001)  # Simulate processing
    shared_counter = temp + amount

def load_large_file(filepath: str) -> list:
    """Load entire file into memory - memory issue."""
    # Loads entire file into memory at once
    with open(filepath, "r") as f:
        return f.readlines()  # No size limit check
