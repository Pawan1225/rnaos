"""
User registry for the RNAOS Enterprise Security Framework.
"""

from __future__ import annotations

from enterprise.security.models import User


class UserRegistry:
    """Registry of platform users."""

    def __init__(self) -> None:
        self._users: dict[str, User] = {}

    def register(
        self,
        user: User,
    ) -> None:
        """Register or update a user."""

        self._users[user.username] = user

    def remove(
        self,
        username: str,
    ) -> None:
        """Remove a user."""

        self._users.pop(username, None)

    def get(
        self,
        username: str,
    ) -> User | None:
        """Retrieve a user."""

        return self._users.get(username)

    def exists(
        self,
        username: str,
    ) -> bool:
        """Check whether a user exists."""

        return username in self._users

    def list_users(
        self,
    ) -> list[User]:
        """Return all registered users."""

        return list(self._users.values())

    def count(
        self,
    ) -> int:
        """Return the number of users."""

        return len(self._users)

    def clear(
        self,
    ) -> None:
        """Remove all users."""

        self._users.clear()
