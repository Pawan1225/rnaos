"""
Backup management for the RNAOS Enterprise Backup Framework.
"""

from __future__ import annotations

from enterprise.backup.models import BackupSnapshot
from enterprise.backup.registry import BackupRegistry


class BackupManager:
    """Manage backup snapshots."""

    def __init__(
        self,
        registry: BackupRegistry | None = None,
    ) -> None:
        self._registry = registry if registry is not None else BackupRegistry()

    def create(
        self,
        snapshot: BackupSnapshot,
    ) -> None:
        """Create a backup."""

        self._registry.register(snapshot)

    def restore(
        self,
        backup_id: str,
    ) -> BackupSnapshot | None:
        """Restore a backup."""

        return self._registry.get(backup_id)

    def exists(
        self,
        backup_id: str,
    ) -> bool:
        """Check whether a backup exists."""

        return self._registry.exists(backup_id)

    def remove(
        self,
        backup_id: str,
    ) -> None:
        """Remove a backup."""

        self._registry.remove(backup_id)

    def list_backups(
        self,
    ) -> list[BackupSnapshot]:
        """Return all backups."""

        return self._registry.list_snapshots()

    def count(
        self,
    ) -> int:
        """Return the number of backups."""

        return self._registry.count()

    def clear(
        self,
    ) -> None:
        """Remove all backups."""

        self._registry.clear()
