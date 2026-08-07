"""
Tests for replica exchange engine.
"""

from __future__ import annotations

from dl.models.optimization.replica_exchange import (
    ReplicaExchangeResult,
)
from dl.optimization.replica_exchange_engine import (
    ReplicaExchangeEngine,
)


def test_replica_exchange_probability() -> None:
    """
    Exchange probability is calculated.
    """

    engine = ReplicaExchangeEngine()

    result = engine.calculate(
        replica_a=1,
        replica_b=2,
        energy_a=-10.0,
        energy_b=-5.0,
        temperature_a=1.0,
        temperature_b=5.0,
    )

    assert isinstance(
        result,
        ReplicaExchangeResult,
    )

    assert result.probability > 0.0
