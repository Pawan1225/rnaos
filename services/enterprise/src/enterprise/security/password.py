"""
Password management for the RNAOS Enterprise Security Framework.
"""

from __future__ import annotations

import hashlib


class PasswordManager:
    """Manage password hashing and verification."""

    def hash_password(
        self,
        password: str,
    ) -> str:
        """Hash a password."""

        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def verify_password(
        self,
        password: str,
        password_hash: str,
    ) -> bool:
        """Verify a password."""

        return self.hash_password(password) == password_hash
