"""
Backup registry for the RNAOS Enterprise Backup Framework.
"""

from __future__ import annotations

from enterprise.backup.models import BackupSnapshot


class BackupRegistry:
    """Registry of backup snapshots."""

    def __init__(self) -> None:
        self._snapshots: dict[str, BackupSnapshot] = {}

    def register(
        self,
        snapshot: BackupSnapshot,
    ) -> None:
        """Register or update a backup snapshot."""

        self._snapshots[snapshot.backup_id] = snapshot

    def get(
        self,
        backup_id: str,
    ) -> BackupSnapshot | None:
        """Retrieve a backup snapshot."""

        return self._snapshots.get(backup_id)

    def exists(
        self,
        backup_id: str,
    ) -> bool:
        """Check whether a backup exists."""

        return backup_id in self._snapshots

    def remove(
        self,
        backup_id: str,
    ) -> None:
        """Remove a backup snapshot."""

        self._snapshots.pop(
            backup_id,
            None,
        )

    def list_snapshots(
        self,
    ) -> list[BackupSnapshot]:
        """Return all backup snapshots."""

        return sorted(
            self._snapshots.values(),
            key=lambda snapshot: snapshot.backup_id,
        )

    def count(
        self,
    ) -> int:
        """Return the number of backups."""

        return len(self._snapshots)

    def clear(
        self,
    ) -> None:
        """Remove all backups."""

        self._snapshots.clear()
