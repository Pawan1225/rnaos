from enterprise.backup import (
    BackupCategory,
    BackupManager,
    BackupSnapshot,
    BackupStatus,
    RecoveryManager,
)


def test_restore_snapshot():

    manager = BackupManager()

    snapshot = BackupSnapshot(
        backup_id="backup-001",
        category=BackupCategory.ARTIFACTS,
        data={"energy": -27.4},
    )

    manager.create(snapshot)

    recovery = RecoveryManager(manager)

    restored = recovery.restore(
        "backup-001",
    )

    assert restored is snapshot

    assert restored.status == BackupStatus.RESTORED


def test_unknown_snapshot():

    manager = BackupManager()

    recovery = RecoveryManager(manager)

    assert (
        recovery.restore(
            "missing",
        )
        is None
    )
