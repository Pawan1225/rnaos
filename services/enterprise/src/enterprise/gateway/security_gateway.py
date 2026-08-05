"""
RNAOS Enterprise Security Gateway.
"""

from __future__ import annotations

from enterprise.security import (
    AuthenticationManager,
    AuthorizationManager,
    PasswordManager,
    TokenManager,
    User,
    UserRegistry,
)


class SecurityGateway:
    """Unified enterprise security interface."""

    def __init__(self) -> None:
        self.registry = UserRegistry()

        self.password = PasswordManager()

        self.authentication = AuthenticationManager(
            registry=self.registry,
            password_manager=self.password,
        )

        self.authorization = AuthorizationManager(
            registry=self.registry,
        )

        self.tokens = TokenManager()

    def count(
        self,
    ) -> int:
        """Return the number of registered users."""

        return self.registry.count()

    def register(
        self,
        user: User,
    ) -> None:
        """Register a user."""

        self.registry.register(user)

    def get(
        self,
        username: str,
    ) -> User | None:
        """Return a user."""

        return self.registry.get(username)

    def exists(
        self,
        username: str,
    ) -> bool:
        """Return whether a user exists."""

        return self.registry.exists(username)

    def remove(
        self,
        username: str,
    ) -> None:
        """Remove a user."""

        self.registry.remove(username)
