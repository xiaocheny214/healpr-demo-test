"""API handler with error handling and security issues."""
import json
import os
import subprocess


def execute_command(user_input: str) -> str:
    """Execute system command - command injection."""
    # Command injection vulnerability
    result = os.system(f"echo {user_input}")
    return str(result)


def parse_json(data: str) -> dict:
    """Parse JSON data - bare exception handling."""
    try:
        return json.loads(data)
    except:  # Bare except - catches everything including SystemExit
        return {}


def read_config(filepath: str) -> dict:
    """Read configuration file - swallowed exception."""
    config = {}
    try:
        with open(filepath, "r") as f:
            config = json.load(f)
    except Exception as e:
        pass  # Silent failure - exception swallowed
    return config


def process_request(request: dict) -> dict:
    """Process API request - missing validation."""
    # No input validation
    action = request["action"]  # KeyError if missing
    data = request["data"]  # KeyError if missing
    
    if action == "delete":
        # No authorization check
        os.remove(data["path"])
        return {"status": "deleted"}
    
    return {"status": "unknown"}

def run_query(sql: str) -> list:
    """Run SQL query - another injection point."""
    import sqlite3
    conn = sqlite3.connect(":memory:")
    # String formatting in SQL
    cursor = conn.execute(f"SELECT * FROM data WHERE id = {sql}")
    return cursor.fetchall()
