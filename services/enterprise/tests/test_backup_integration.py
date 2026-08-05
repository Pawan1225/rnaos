from enterprise.backup import (
    BackupCategory,
    BackupManager,
    BackupSnapshot,
    BackupStatus,
    RecoveryManager,
)


def test_backup_workflow():
    """End-to-end backup and recovery workflow."""

    manager = BackupManager()

    snapshot = BackupSnapshot(
        backup_id="experiment-001",
        category=BackupCategory.EXPERIMENTS,
        data={
            "sequence": "AUGCGGAU",
            "energy": -27.4,
        },
    )

    manager.create(snapshot)

    assert manager.count() == 1
    assert manager.exists("experiment-001")

    recovery = RecoveryManager(manager)

    restored = recovery.restore("experiment-001")

    assert restored is not None
    assert restored.backup_id == "experiment-001"
    assert restored.category == BackupCategory.EXPERIMENTS
    assert restored.status == BackupStatus.RESTORED
    assert restored.data["energy"] == -27.4
