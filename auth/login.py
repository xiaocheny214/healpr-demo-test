"""Authentication module with security issues."""
import hashlib
import sqlite3
import os

# Hardcoded credentials - security issue
DB_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"
SECRET_TOKEN = "my-super-secret-token-do-not-share"


def hash_password(password: str) -> str:
    """Hash password using MD5 - weak hashing."""
    return hashlib.md5(password.encode()).hexdigest()


def verify_user(username: str, password: str) -> bool:
    """Verify user credentials - SQL injection vulnerability."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{hash_password(password)}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result is not None


def create_session(user_id: int) -> str:
    """Create session with predictable token."""
    # Predictable session token
    import time
    return hashlib.md5(f"{user_id}-{int(time.time())}".encode()).hexdigest()


def get_user_data(user_id: str) -> dict:
    """Get user data - path traversal vulnerability."""
    # Path traversal vulnerability
    filepath = f"/data/users/{user_id}/profile.json"
    with open(filepath, "r") as f:
        return eval(f.read())  # eval is dangerous
