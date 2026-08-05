"""
Authorization management for the RNAOS Enterprise Security Framework.
"""

from __future__ import annotations

from enterprise.security.registry import UserRegistry


class AuthorizationManager:
    """Authorize platform users."""

    def __init__(
        self,
        registry: UserRegistry,
    ) -> None:
        self._registry = registry

    def has_role(
        self,
        username: str,
        role: str,
    ) -> bool:
        """Check whether a user has the specified role."""

        user = self._registry.get(username)

        if user is None:
            return False

        return user.role == role

    def has_permission(
        self,
        username: str,
        permission: str,
    ) -> bool:
        """Check whether a user has the specified permission."""

        user = self._registry.get(username)

        if user is None:
            return False

        permissions = user.metadata.get(
            "permissions",
            set(),
        )

        return permission in permissions

    def authorize(
        self,
        username: str,
        role: str | None = None,
        permission: str | None = None,
    ) -> bool:
        """Authorize a user."""

        return (role is None or self.has_role(username, role)) and (
            permission is None
            or self.has_permission(
                username,
                permission,
            )
        )
