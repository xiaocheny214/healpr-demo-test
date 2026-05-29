"""User model with anti-patterns and code smells."""
from datetime import datetime
import re


class User:
    def __init__(self, name, email, age, role, password):
        # No input validation
        self.name = name
        self.email = email
        self.age = age
        self.role = role
        self._password = password  # Storing plain text password
        self.created_at = datetime.now()
        self.login_attempts = 0
        self.is_active = True
    
    def validate_email(self):
        """Validate email - overly complex regex."""
        # Overly complex and incorrect email regex
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(pattern, self.email))
    
    def check_password(self, password: str) -> bool:
        """Check password - timing attack vulnerable."""
        # Direct string comparison - timing attack
        return self._password == password
    
    def update_email(self, new_email: str):
        """Update email - no validation."""
        self.email = new_email  # No validation performed
    
    def to_dict(self) -> dict:
        """Convert to dictionary - exposes password."""
        # Password exposed in serialization
        return {
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "role": self.role,
            "password": self._password,  # Security issue
            "created_at": str(self.created_at),
            "login_attempts": self.login_attempts
        }
    
    def __eq__(self, other):
        """Equality check - missing type check."""
        # Will raise AttributeError if other is not User
        return self.email == other.email
    
    def __repr__(self):
        """String representation - exposes sensitive data."""
        return f"User({self.name}, {self.email}, role={self.role}, pw={self._password})"
