"""
Tests for replica manager.
"""

from __future__ import annotations

from dl.models.optimization.replica_pool import (
    ReplicaPool,
)
from dl.optimization.replica_manager import (
    ReplicaManager,
)


def test_replica_creation() -> None:
    """
    Replica manager creates replicas.
    """

    manager = ReplicaManager()

    pool = manager.create(
        temperatures=(
            1.0,
            5.0,
            10.0,
        ),
    )

    assert isinstance(
        pool,
        ReplicaPool,
    )

    assert (
        len(
            pool.replicas,
        )
        == 3
    )
