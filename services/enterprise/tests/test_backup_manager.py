from enterprise.backup import (
    BackupCategory,
    BackupManager,
    BackupSnapshot,
)


def test_create_backup():

    manager = BackupManager()

    manager.create(
        BackupSnapshot(
            backup_id="backup-001",
            category=BackupCategory.ARTIFACTS,
            data={},
        )
    )

    assert manager.count() == 1


def test_restore_backup():

    manager = BackupManager()

    snapshot = BackupSnapshot(
        backup_id="backup-001",
        category=BackupCategory.ANALYTICS,
        data={},
    )

    manager.create(snapshot)

    assert manager.restore("backup-001") is snapshot


def test_exists():

    manager = BackupManager()

    manager.create(
        BackupSnapshot(
            backup_id="backup-001",
            category=BackupCategory.CONFIGURATION,
            data={},
        )
    )

    assert manager.exists("backup-001")


def test_remove():

    manager = BackupManager()

    manager.create(
        BackupSnapshot(
            backup_id="backup-001",
            category=BackupCategory.CACHE,
            data={},
        )
    )

    manager.remove("backup-001")

    assert manager.count() == 0


def test_list_backups():

    manager = BackupManager()

    manager.create(
        BackupSnapshot(
            backup_id="b",
            category=BackupCategory.ARTIFACTS,
            data={},
        )
    )

    manager.create(
        BackupSnapshot(
            backup_id="a",
            category=BackupCategory.ANALYTICS,
            data={},
        )
    )

    backups = manager.list_backups()

    assert len(backups) == 2

    assert backups[0].backup_id == "a"
