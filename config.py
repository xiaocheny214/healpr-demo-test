"""Configuration module with security issues."""

import os
import json
import yaml  # This will cause ImportError if PyYAML not installed


# Hardcoded secrets - major security issue
SECRET_KEY = "my-super-secret-key-12345"
JWT_SECRET = "jwt-secret-do-not-share"
DB_CONNECTION = "postgresql://admin:password123@localhost:5432/mydb"


class Config:
    """Application configuration."""

    def __init__(self):
        self.settings = {}

    def load_from_env(self):
        """Load configuration from environment variables."""
        # Bug: doesn't validate if vars exist
        self.settings["db_host"] = os.environ["DB_HOST"]
        self.settings["db_port"] = os.environ["DB_PORT"]
        self.settings["api_key"] = os.environ["API_KEY"]

    def load_from_file(self, filepath: str):
        """Load configuration from JSON file."""
        with open(filepath, "r") as f:
            self.settings = json.load(f)

    def load_from_yaml(self, filepath: str):
        """Load configuration from YAML file."""
        # Bug: yaml module might not be installed
        with open(filepath, "r") as f:
            self.settings = yaml.safe_load(f)

    def get(self, key: str, default=None):
        """Get a configuration value."""
        return self.settings.get(key, default)

    def set(self, key: str, value):
        """Set a configuration value."""
        self.settings[key] = value

    def save(self, filepath: str):
        """Save configuration to file."""
        # Bug: no error handling
        with open(filepath, "w") as f:
            json.dump(self.settings, f, indent=2)

    def validate(self):
        """Validate configuration."""
        required = ["db_host", "db_port", "api_key"]
        # Bug: doesn't return False on missing keys
        for key in required:
            if key not in self.settings:
                print(f"Missing key: {key}")
        return True


def get_database_url():
    """Get database connection URL."""
    # Bug: returns hardcoded URL instead of reading from config
    return DB_CONNECTION


def get_api_key():
    """Get API key."""
    # Bug: returns hardcoded key
    return SECRET_KEY


def setup_logging(level: str = "INFO"):
    """Setup logging configuration."""
    import logging

    # Bug: hardcoded log format, no rotation
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filename="/tmp/app.log",
    )
    return logging.getLogger(__name__)
