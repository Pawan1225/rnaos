"""
Recovery management for the RNAOS Enterprise Backup Framework.
"""

from __future__ import annotations

from enterprise.backup.manager import BackupManager
from enterprise.backup.models import (
    BackupSnapshot,
    BackupStatus,
)


class RecoveryManager:
    """Restore backup snapshots."""

    def __init__(
        self,
        manager: BackupManager,
    ) -> None:
        self._manager = manager

    def restore(
        self,
        backup_id: str,
    ) -> BackupSnapshot | None:
        """Restore a backup snapshot."""

        snapshot = self._manager.restore(
            backup_id,
        )

        if snapshot is not None:
            snapshot.status = BackupStatus.RESTORED

        return snapshot
