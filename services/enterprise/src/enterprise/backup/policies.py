"""
Backup policies for the RNAOS Enterprise Backup Framework.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from enterprise.backup.models import BackupSnapshot


class BackupPolicy(ABC):
    """Abstract backup policy."""

    @abstractmethod
    def should_backup(
        self,
        snapshot: BackupSnapshot,
    ) -> bool:
        """Determine whether a backup should be created."""


class ManualBackupPolicy(BackupPolicy):
    """Always allow manual backups."""

    def should_backup(
        self,
        snapshot: BackupSnapshot,
    ) -> bool:
        return True
