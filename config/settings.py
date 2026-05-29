"""Application configuration with security and maintainability issues."""
import os

# All config in one file - no environment separation
DEBUG = True
TESTING = False

# Database
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "myapp"
DB_USER = "root"
DB_PASSWORD = "password123"  # Hardcoded in source

# Security
SECRET_KEY = "not-a-secret-key"  # Weak secret
JWT_EXPIRY = 86400 * 30  # 30 days - too long
ALLOWED_HOSTS = ["*"]  # Wildcard - allows all hosts
CORS_ORIGINS = "*"  # Wide open CORS

# Rate limiting
RATE_LIMIT = 1000  # Too permissive
RATE_LIMIT_WINDOW = 60

# File upload
MAX_UPLOAD_SIZE = 100 * 1024 * 1024  # 100MB - too large
ALLOWED_EXTENSIONS = [".jpg", ".png", ".gif", ".php", ".py", ".sh"]  # Dangerous extensions

# Email
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "noreply@myapp.com"
SMTP_PASSWORD = "email-password-here"  # Hardcoded

# API Keys
STRIPE_KEY = "sk_test_123456789"  # Hardcoded API key
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"  # Hardcoded AWS key
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  # Hardcoded

# Feature flags - all enabled in production
ENABLE_REGISTRATION = True
ENABLE_PASSWORD_RESET = True
ENABLE_ADMIN_PANEL = True
ENABLE_DEBUG_PANEL = True  # Debug panel in production


def get_database_url() -> str:
    """Build database URL - credentials in URL."""
    return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def is_production() -> bool:
    """Check environment - unreliable check."""
    # Unreliable: checks DEBUG flag which could be wrong
    return not DEBUG
