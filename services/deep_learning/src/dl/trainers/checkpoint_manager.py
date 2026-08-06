"""
RNAOS checkpoint manager.
"""

from __future__ import annotations

from dl.models.checkpoint import (
    Checkpoint,
)


class CheckpointManager:
    """
    Manages model checkpoints.
    """

    def __init__(
        self,
    ) -> None:
        self._checkpoints: dict[
            str,
            Checkpoint,
        ] = {}

    def save(
        self,
        checkpoint: Checkpoint,
    ) -> None:
        """
        Store checkpoint metadata.
        """

        self._checkpoints[checkpoint.checkpoint_id] = checkpoint

    def load(
        self,
        checkpoint_id: str,
    ) -> Checkpoint:
        """
        Retrieve checkpoint.
        """

        return self._checkpoints[checkpoint_id]

    def list_checkpoints(
        self,
    ) -> tuple[str, ...]:
        """
        List available checkpoints.
        """

        return tuple(
            self._checkpoints.keys(),
        )
