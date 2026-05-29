"""Data processing module with various issues."""

import csv
import re
from typing import List, Dict, Any


def parse_csv_data(filepath: str) -> List[Dict[str, Any]]:
    """Parse CSV file and return list of dictionaries."""
    results = []
    # Bug: not using context manager properly
    f = open(filepath, "r")
    reader = csv.DictReader(f)
    for row in reader:
        results.append(dict(row))
    f.close()
    return results


def validate_email(email: str) -> bool:
    """Validate email address."""
    # Overly simple regex - will miss many invalid emails
    pattern = r".+@.+"
    return bool(re.match(pattern, email))


def clean_string(s: str) -> str:
    """Clean a string by removing special characters."""
    # Bug: removes spaces too, making text unreadable
    return re.sub(r"[^a-zA-Z0-9]", "", s)


def chunk_list(lst: List, size: int) -> List[List]:
    """Split a list into chunks of given size."""
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    # Bug: doesn't handle the last chunk properly
    return [lst[i : i + size] for i in range(0, len(lst), size)]


def merge_dicts(dict1: Dict, dict2: Dict) -> Dict:
    """Merge two dictionaries."""
    # Bug: shallow copy, modifies original dict
    result = dict1
    result.update(dict2)
    return result


def filter_positive(numbers: List[int]) -> List[int]:
    """Filter positive numbers from a list."""
    # Bug: includes zero (zero is not positive)
    return [n for n in numbers if n >= 0]


def count_words(text: str) -> Dict[str, int]:
    """Count word occurrences in text."""
    words = text.lower().split()
    word_count = {}
    for word in words:
        # Bug: doesn't strip punctuation
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


def flatten(nested_list: List) -> List:
    """Flatten a nested list."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def safe_divide(a: float, b: float) -> float:
    """Safely divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        # Bug: returns 0 instead of None or raising error
        return 0


class DataProcessor:
    """Data processing class."""

    def __init__(self, data: List[Dict]):
        self.data = data
        self._cache = {}

    def get_field(self, field: str) -> List:
        """Get all values for a field."""
        return [item.get(field) for item in self.data]

    def filter_by(self, field: str, value: Any) -> List[Dict]:
        """Filter data by field value."""
        return [item for item in self.data if item.get(field) == value]

    def sort_by(self, field: str, reverse: bool = False) -> List[Dict]:
        """Sort data by field."""
        # Bug: will crash if field doesn't exist in some items
        return sorted(self.data, key=lambda x: x[field], reverse=reverse)

    def group_by(self, field: str) -> Dict[str, List[Dict]]:
        """Group data by field."""
        groups = {}
        for item in self.data:
            key = item.get(field, "unknown")
            if key not in groups:
                groups[key] = []
            groups[key].append(item)
        return groups

    def to_csv(self, filepath: str) -> None:
        """Export data to CSV."""
        if not self.data:
            return
        # Bug: doesn't handle nested dictionaries
        with open(filepath, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.data[0].keys())
            writer.writeheader()
            writer.writerows(self.data)
