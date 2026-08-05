"""
Domain models for the RNAOS Enterprise Security Framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum


class UserStatus(StrEnum):
    """User account status."""

    ACTIVE = "active"
    DISABLED = "disabled"
    LOCKED = "locked"


@dataclass(slots=True, frozen=True)
class Permission:
    """Platform permission."""

    name: str
    description: str = ""


@dataclass(slots=True)
class Role:
    """Platform role."""

    name: str
    description: str = ""

    permissions: set[str] = field(
        default_factory=set,
    )

    def add_permission(
        self,
        permission: str,
    ) -> None:
        """Add a permission."""

        self.permissions.add(permission)

    def has_permission(
        self,
        permission: str,
    ) -> bool:
        """Check whether the role grants a permission."""

        return permission in self.permissions


@dataclass(slots=True)
class User:
    """Enterprise platform user."""

    username: str

    role: str

    email: str | None = None

    display_name: str | None = None

    status: UserStatus = UserStatus.ACTIVE

    metadata: dict[str, object] = field(
        default_factory=dict,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    last_login: datetime | None = None


@dataclass(slots=True)
class Session:
    """Authenticated user session."""

    session_id: str

    username: str

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    expires_at: datetime | None = None


@dataclass(slots=True)
class ApiToken:
    """API token."""

    token: str

    username: str

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    expires_at: datetime | None = None

    revoked: bool = False
