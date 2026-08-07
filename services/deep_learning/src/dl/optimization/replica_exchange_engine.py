"""
RNAOS replica exchange engine.
"""

from __future__ import annotations

import math

from dl.models.optimization.replica_exchange import (
    ReplicaExchangeResult,
)


class ReplicaExchangeEngine:
    """
    Calculates replica exchange decisions.
    """

    def calculate(
        self,
        replica_a: int,
        replica_b: int,
        energy_a: float,
        energy_b: float,
        temperature_a: float,
        temperature_b: float,
    ) -> ReplicaExchangeResult:
        """
        Calculate exchange probability.
        """

        delta = ((1 / temperature_a) - (1 / temperature_b)) * (energy_b - energy_a)

        probability = min(
            1.0,
            math.exp(
                delta,
            ),
        )

        return ReplicaExchangeResult(
            replica_a=replica_a,
            replica_b=replica_b,
            accepted=(probability >= 0.5),
            probability=probability,
        )
