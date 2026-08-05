"""
Domain models for the RNAOS Enterprise Backup Framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import StrEnum
from typing import Any


class BackupCategory(StrEnum):
    """Backup categories."""

    ARTIFACTS = "artifacts"
    ANALYTICS = "analytics"
    CONFIGURATION = "configuration"
    EXPERIMENTS = "experiments"
    CACHE = "cache"


class BackupStatus(StrEnum):
    """Backup lifecycle."""

    CREATED = "created"
    STORED = "stored"
    RESTORED = "restored"
    FAILED = "failed"


@dataclass(slots=True)
class BackupSnapshot:
    """Backup snapshot."""

    backup_id: str

    category: BackupCategory

    data: Any

    status: BackupStatus = BackupStatus.CREATED

    metadata: dict[str, object] = field(
        default_factory=dict,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )
