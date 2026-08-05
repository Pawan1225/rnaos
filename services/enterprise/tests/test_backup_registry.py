from enterprise.backup import (
    BackupCategory,
    BackupRegistry,
    BackupSnapshot,
)


def test_register_snapshot():

    registry = BackupRegistry()

    registry.register(
        BackupSnapshot(
            backup_id="backup-001",
            category=BackupCategory.ARTIFACTS,
            data={},
        )
    )

    assert registry.count() == 1


def test_lookup_snapshot():

    registry = BackupRegistry()

    snapshot = BackupSnapshot(
        backup_id="backup-001",
        category=BackupCategory.ANALYTICS,
        data={},
    )

    registry.register(snapshot)

    assert registry.get("backup-001") is snapshot


def test_remove_snapshot():

    registry = BackupRegistry()

    registry.register(
        BackupSnapshot(
            backup_id="backup-001",
            category=BackupCategory.CONFIGURATION,
            data={},
        )
    )

    registry.remove("backup-001")

    assert registry.count() == 0


def test_exists():

    registry = BackupRegistry()

    registry.register(
        BackupSnapshot(
            backup_id="backup-001",
            category=BackupCategory.EXPERIMENTS,
            data={},
        )
    )

    assert registry.exists("backup-001")

    assert not registry.exists("missing")


def test_clear():

    registry = BackupRegistry()

    registry.register(
        BackupSnapshot(
            backup_id="a",
            category=BackupCategory.ARTIFACTS,
            data={},
        )
    )

    registry.register(
        BackupSnapshot(
            backup_id="b",
            category=BackupCategory.ANALYTICS,
            data={},
        )
    )

    registry.clear()

    assert registry.count() == 0
