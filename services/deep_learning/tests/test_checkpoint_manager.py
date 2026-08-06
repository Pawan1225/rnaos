"""
Tests for checkpoint manager.
"""

from __future__ import annotations

from dl.models.checkpoint import (
    Checkpoint,
)
from dl.trainers.checkpoint_manager import (
    CheckpointManager,
)


def create_checkpoint() -> Checkpoint:
    """
    Create deterministic checkpoint.
    """

    return Checkpoint(
        checkpoint_id="checkpoint_001",
        model_name="transformer",
        epoch=10,
        path="/tmp/model.ckpt",
        created_at="2026-08-06",
    )


def test_save_checkpoint() -> None:
    """
    Checkpoint is stored.
    """

    manager = CheckpointManager()

    checkpoint = create_checkpoint()

    manager.save(
        checkpoint,
    )

    assert "checkpoint_001" in manager.list_checkpoints()


def test_load_checkpoint() -> None:
    """
    Checkpoint can be retrieved.
    """

    manager = CheckpointManager()

    checkpoint = create_checkpoint()

    manager.save(
        checkpoint,
    )

    result = manager.load(
        "checkpoint_001",
    )

    assert result == checkpoint


def test_multiple_checkpoints() -> None:
    """
    Multiple checkpoints are supported.
    """

    manager = CheckpointManager()

    manager.save(
        create_checkpoint(),
    )

    second = Checkpoint(
        checkpoint_id="checkpoint_002",
        model_name="cnn",
        epoch=20,
        path="/tmp/cnn.ckpt",
        created_at="2026-08-06",
    )

    manager.save(
        second,
    )

    assert manager.list_checkpoints() == (
        "checkpoint_001",
        "checkpoint_002",
    )
