#!/usr/bin/env python3
"""
Python utility for user data validation and processing
Optional utility for data analytics and validation
"""

import re
import hashlib
import mysql.connector
from typing import Dict, Optional, Tuple

class UserDataValidator:
    def __init__(self, db_config: Optional[Dict] = None):
        self.db_config = db_config or {
            'host': 'localhost',
            'user': 'root',
            'password': 'password',
            'database': 'user_registration'
        }
    
    def validate_username(self, username: str) -> Tuple[bool, str]:
        """Validate username format and uniqueness"""
        if len(username) < 3:
            return False, "Username must be at least 3 characters long"
        if len(username) > 50:
            return False, "Username must be less than 50 characters"
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return False, "Username can only contain letters, numbers, and underscores"
        
        # Check uniqueness in database
        if self.db_config and self._username_exists(username):
            return False, "Username already exists"
        
        return True, "Username is valid"
    
    def validate_email(self, email: str) -> Tuple[bool, str]:
        """Validate email format and uniqueness"""
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            return False, "Invalid email format"
        
        # Check uniqueness in database
        if self.db_config and self._email_exists(email):
            return False, "Email already exists"
        
        return True, "Email is valid"
    
    def validate_password(self, password: str) -> Tuple[bool, str]:
        """Validate password strength"""
        if len(password) < 6:
            return False, "Password must be at least 6 characters long"
        if not any(char.isdigit() for char in password):
            return False, "Password must contain at least one digit"
        if not any(char.isupper() for char in password):
            return False, "Password must contain at least one uppercase letter"
        if not any(char.islower() for char in password):
            return False, "Password must contain at least one lowercase letter"
        
        return True, "Password is strong"
    
    def hash_password(self, password: str) -> str:
        """Hash password using SHA-256 (for demonstration, use bcrypt in production)"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def _username_exists(self, username: str) -> bool:
        """Check if username exists in database"""
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
            count = cursor.fetchone()[0]
            return count > 0
        except mysql.connector.Error:
            return False
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()
    
    def _email_exists(self, email: str) -> bool:
        """Check if email exists in database"""
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM users WHERE email = %s", (email,))
            count = cursor.fetchone()[0]
            return count > 0
        except mysql.connector.Error:
            return False
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

def validate_user_data(username: str, email: str, password: str) -> Dict:
    """Convenience function to validate all user data"""
    validator = UserDataValidator()
    
    results = {
        'username': validator.validate_username(username),
        'email': validator.validate_email(email),
        'password': validator.validate_password(password),
        'overall_valid': True,
        'errors': []
    }
    
    # Check if all validations passed
    for field, (is_valid, message) in results.items():
        if field != 'overall_valid' and field != 'errors':
            if not is_valid:
                results['overall_valid'] = False
                results['errors'].append(f"{field.capitalize()}: {message}")
    
    return results

if __name__ == "__main__":
    # Example usage
    test_data = [
        ("john_doe", "john@example.com", "Password123"),
        ("jd", "invalid-email", "weak"),
        ("test_user", "test@example.com", "StrongPass1")
    ]
    
    for username, email, password in test_data:
        print(f"\nTesting: {username}, {email}, {password}")
        result = validate_user_data(username, email, password)
        print(f"Valid: {result['overall_valid']}")
        if result['errors']:
            print("Errors:", result['errors'])
        else:
            print("All validations passed!")
