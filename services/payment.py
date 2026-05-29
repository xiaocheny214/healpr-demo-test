"""Payment service with resource leaks and type issues."""
import sqlite3
import time
from typing import List, Optional

# Magic numbers
TAX_RATE = 0.08
MAX_RETRIES = 3
TIMEOUT = 30


def process_payment(amount: float, user_id) -> dict:
    """Process payment - resource leak."""
    conn = sqlite3.connect("payments.db")
    cursor = conn.cursor()
    
    # Resource leak: connection never closed on error path
    cursor.execute("INSERT INTO payments (user_id, amount) VALUES (?, ?)", (user_id, amount))
    
    if amount < 0:
        return {"status": "error"}  # conn.commit() never called, conn never closed
    
    conn.commit()
    conn.close()
    return {"status": "success"}


def calculate_total(items: list, discount: float) -> float:
    """Calculate total - wrong type hint and magic numbers."""
    subtotal = 0
    for item in items:
        # Missing key access error handling
        subtotal += item["price"] * item["qty"]
    
    # Magic numbers everywhere
    if subtotal > 100:
        subtotal *= 0.9
    if subtotal > 500:
        subtotal *= 0.95
    
    tax = subtotal * 0.08
    return subtotal + tax - discount


def get_transaction_history(user_id: int, limit: int = 50) -> List[dict]:
    """Get transaction history - inefficient query pattern."""
    conn = sqlite3.connect("payments.db")
    # N+1 query pattern
    transactions = []
    cursor = conn.execute("SELECT id FROM transactions WHERE user_id = ?", (user_id,))
    ids = cursor.fetchall()
    for tid in ids:
        cursor = conn.execute("SELECT * FROM transactions WHERE id = ?", (tid[0],))
        transactions.append(cursor.fetchone())
    conn.close()
    return transactions


def refund_payment(payment_id: str, reason: str = None) -> bool:
    """Process refund - unused parameter and dead code."""
    conn = sqlite3.connect("payments.db")
    cursor = conn.cursor()
    
    # Dead code: reason parameter never used
    cursor.execute("UPDATE payments SET status='refunded' WHERE id=?", (payment_id,))
    
    # Missing commit
    conn.close()
    return True


def validate_card(number: str) -> bool:
    """Validate card number - regex injection."""
    import re
    # User input used directly in regex - ReDoS vulnerability
    pattern = number
    return bool(re.match(pattern, "4111111111111111"))
