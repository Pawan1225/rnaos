"""
Authentication management for the RNAOS Enterprise Security Framework.
"""

from __future__ import annotations

from enterprise.security.password import PasswordManager
from enterprise.security.registry import UserRegistry


class AuthenticationManager:
    """Authenticate platform users."""

    def __init__(
        self,
        registry: UserRegistry,
        password_manager: PasswordManager | None = None,
    ) -> None:
        self._registry = registry
        self._password_manager = (
            password_manager if password_manager is not None else PasswordManager()
        )

    def authenticate_username(
        self,
        username: str,
    ) -> bool:
        """Authenticate by username."""

        return self._registry.exists(username)

    def authenticate_password(
        self,
        username: str,
        password: str,
        password_hash: str,
    ) -> bool:
        """Authenticate using a password."""

        if not self._registry.exists(username):
            return False

        return self._password_manager.verify_password(
            password,
            password_hash,
        )
