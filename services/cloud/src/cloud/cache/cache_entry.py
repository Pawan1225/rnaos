"""
RNAOS cache entry.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from typing import Any


@dataclass(slots=True, frozen=True)
class CacheEntry:
    """Immutable cache entry."""

    key: str

    value: Any

    ttl: int | None = None

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    def is_expired(self) -> bool:
        """Return True if this cache entry has expired."""
        if self.ttl is None:
            return False

        expires_at = self.created_at + timedelta(
            seconds=self.ttl,
        )

        return datetime.now(UTC) >= expires_at
