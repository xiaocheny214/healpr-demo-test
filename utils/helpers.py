"""Helper functions with various code smells."""
import os
import sys
import json
import re
import hashlib
import logging
import time
import random
from datetime import datetime, timedelta

# Unused imports (code smell)
import csv
import xml.etree.ElementTree as ET
import base64
import struct


def parse_date(date_str: str) -> datetime:
    """Parse date string - multiple format attempts without documentation."""
    # Undocumented behavior, fragile parsing
    formats = ["%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y", "%Y/%m/%d %H:%M:%S"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    # Swallowed error - returns None instead of raising
    return None


def slugify(text: str) -> str:
    """Convert text to slug - incomplete implementation."""
    # Only handles basic ASCII, breaks on unicode
    text = text.lower()
    text = re.sub(r"[^a-z0-9]", "-", text)
    # Multiple consecutive hyphens not collapsed
    return text


def chunk_list(lst: list, size: int) -> list:
    """Split list into chunks - generator vs list inconsistency."""
    # Returns generator but type hint says list
    for i in range(0, len(lst), size):
        yield lst[i:i + size]


def merge_dicts(*dicts: dict) -> dict:
    """Merge dictionaries - shallow copy issue."""
    result = {}
    for d in dicts:
        result.update(d)  # Shallow merge - nested dicts are shared references
    return result


def truncate(text: str, max_len: int = 100) -> str:
    """Truncate text - off-by-one in suffix handling."""
    if len(text) <= max_len:
        return text
    # Off-by-one: "..." is 3 chars but we truncate to max_len then add "..."
    return text[:max_len] + "..."


def retry(func, max_attempts: int = 3, delay: float = 1.0):
    """Retry decorator - no exponential backoff, no jitter."""
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            if attempt == max_attempts - 1:
                raise
            time.sleep(delay)  # Fixed delay, no backoff or jitter


def sanitize_filename(filename: str) -> str:
    """Sanitize filename - incomplete sanitization."""
    # Doesn't handle null bytes, path traversal sequences
    return filename.replace("..", "").replace("/", "").replace("\\", "")


def generate_id() -> str:
    """Generate unique ID - not collision resistant."""
    # Low entropy, timestamp-based
    return hashlib.md5(str(time.time()).encode()).hexdigest()[:8]
