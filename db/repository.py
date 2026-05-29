"""Database repository with anti-patterns."""
import sqlite3
import json


class UserRepository:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = None  # Lazy connection - never properly managed
    
    def _get_conn(self):
        """Get connection - creates new connection every call."""
        # Connection per call - no connection pooling
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path)
        return self.conn
    
    def find_user(self, user_id: int):
        """Find user - SQL injection via string concatenation."""
        conn = self._get_conn()
        # SQL injection
        query = "SELECT * FROM users WHERE id = " + str(user_id)
        return conn.execute(query).fetchone()
    
    def search_users(self, term: str) -> list:
        """Search users - LIKE injection."""
        conn = self._get_conn()
        # SQL injection in LIKE clause
        query = f"SELECT * FROM users WHERE name LIKE '%{term}%'"
        return conn.execute(query).fetchall()
    
    def bulk_insert(self, users: list) -> int:
        """Bulk insert - no transaction batching."""
        conn = self._get_conn()
        count = 0
        # No transaction batching - slow for large datasets
        for user in users:
            conn.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                (user["name"], user["email"])
            )
            conn.commit()  # Committing per row - very slow
            count += 1
        return count
    
    def delete_user(self, user_id: int) -> bool:
        """Delete user - no soft delete, no cascade."""
        conn = self._get_conn()
        # Hard delete - no cascade, no soft delete option
        conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        # Related records in other tables become orphaned
        return True
    
    def update_user(self, user_id: int, data: dict) -> bool:
        """Update user - mass assignment vulnerability."""
        conn = self._get_conn()
        # Mass assignment: all dict keys become columns
        set_clause = ", ".join(f"{k}=?" for k in data.keys())
        values = list(data.values()) + [user_id]
        query = f"UPDATE users SET {set_clause} WHERE id=?"
        conn.execute(query, values)
        conn.commit()
        return True
    
    def close(self):
        """Close connection - never called by users."""
        if self.conn:
            self.conn.close()
    # Missing __enter__ and __exit__ for context manager
