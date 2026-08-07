"""
Tests for parallel tempering engine.
"""

from __future__ import annotations

from dl.models.optimization.parallel_tempering_result import (
    ParallelTemperingResult,
)
from dl.models.optimization.replica_pool import (
    ReplicaPool,
)
from dl.models.optimization.temperature_replica import (
    TemperatureReplica,
)
from dl.optimization.parallel_tempering_engine import (
    ParallelTemperingEngine,
)


def test_parallel_tempering_selects_best_replica() -> None:
    """
    Lowest energy replica is selected.
    """

    pool = ReplicaPool(
        replicas=(
            TemperatureReplica(
                replica_id=1,
                temperature=1.0,
                state=(),
                energy=-5.0,
            ),
            TemperatureReplica(
                replica_id=2,
                temperature=5.0,
                state=(),
                energy=-10.0,
            ),
        ),
    )

    engine = ParallelTemperingEngine()

    result = engine.optimize(
        pool,
    )

    assert isinstance(
        result,
        ParallelTemperingResult,
    )

    assert result.best_replica_id == 2

    assert result.best_energy == -10.0
