"""
Tests for temperature replica.
"""

from __future__ import annotations

from dl.models.optimization.temperature_replica import (
    TemperatureReplica,
)


def test_temperature_replica_creation() -> None:
    """
    Replica model can be created.
    """

    replica = TemperatureReplica(
        replica_id=1,
        temperature=10.0,
        state=(
            1,
            -1,
            1,
        ),
        energy=-5.0,
    )

    assert replica.replica_id == 1

    assert replica.temperature == 10.0

    assert replica.energy == -5.0
