"""
Tests for parallel tempering profile engine.
"""

from __future__ import annotations

from dl.models.optimization.parallel_tempering_profile import (
    ParallelTemperingProfile,
)
from dl.optimization.parallel_tempering_profile_engine import (
    ParallelTemperingProfileEngine,
)


def test_profile_generation() -> None:
    """
    Parallel tempering profile is generated.
    """

    engine = ParallelTemperingProfileEngine()

    profile = engine.generate(
        best_replica_id=2,
        best_energy=-10.0,
        replica_count=5,
        exchanges=4,
    )

    assert isinstance(
        profile,
        ParallelTemperingProfile,
    )

    assert profile.best_energy == -10.0

    assert profile.exchanges == 4
