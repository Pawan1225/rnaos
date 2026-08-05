from enterprise.backup import (
    BackupCategory,
    BackupSnapshot,
    ManualBackupPolicy,
)


def test_manual_policy():

    policy = ManualBackupPolicy()

    snapshot = BackupSnapshot(
        backup_id="backup-001",
        category=BackupCategory.ARTIFACTS,
        data={},
    )

    assert policy.should_backup(snapshot)
