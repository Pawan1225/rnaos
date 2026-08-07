"""
RNAOS parallel tempering engine.
"""

from __future__ import annotations

from dl.models.optimization.parallel_tempering_result import (
    ParallelTemperingResult,
)
from dl.models.optimization.replica_pool import (
    ReplicaPool,
)


class ParallelTemperingEngine:
    """
    Executes parallel tempering optimization.
    """

    def optimize(
        self,
        pool: ReplicaPool,
    ) -> ParallelTemperingResult:
        """
        Select lowest energy replica.
        """

        if not pool.replicas:
            raise ValueError(
                "Replica pool cannot be empty",
            )

        best = min(
            pool.replicas,
            key=lambda replica: replica.energy,
        )

        return ParallelTemperingResult(
            best_replica_id=best.replica_id,
            best_energy=best.energy,
            exchanges=len(
                pool.replicas,
            )
            - 1,
            converged=True,
        )
