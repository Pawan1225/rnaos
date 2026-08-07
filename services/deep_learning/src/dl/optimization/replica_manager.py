"""
RNAOS replica manager.
"""

from __future__ import annotations

from dl.models.optimization.replica_pool import (
    ReplicaPool,
)
from dl.models.optimization.temperature_replica import (
    TemperatureReplica,
)


class ReplicaManager:
    """
    Creates and manages temperature replicas.
    """

    def create(
        self,
        temperatures: tuple[float, ...],
    ) -> ReplicaPool:
        """
        Create replica population.
        """

        replicas = tuple(
            TemperatureReplica(
                replica_id=index,
                temperature=temperature,
                state=(),
                energy=0.0,
            )
            for index, temperature in enumerate(
                temperatures,
            )
        )

        return ReplicaPool(
            replicas=replicas,
        )
