from enterprise.backup import (
    BackupCategory,
    BackupSnapshot,
    BackupStatus,
)


def test_snapshot_defaults():

    snapshot = BackupSnapshot(
        backup_id="backup-001",
        category=BackupCategory.ARTIFACTS,
        data={"energy": -27.4},
    )

    assert snapshot.status == BackupStatus.CREATED

    assert snapshot.metadata == {}


def test_category():

    assert BackupCategory.CONFIGURATION == "configuration"


def test_status():

    assert BackupStatus.RESTORED == "restored"
