"""
RNAOS parallel tempering profile engine.
"""

from __future__ import annotations

from dl.models.optimization.parallel_tempering_profile import (
    ParallelTemperingProfile,
)


class ParallelTemperingProfileEngine:
    """
    Generates parallel tempering profiles.
    """

    def generate(
        self,
        best_replica_id: int,
        best_energy: float,
        replica_count: int,
        exchanges: int,
    ) -> ParallelTemperingProfile:
        """
        Generate intelligence profile.
        """

        confidence = min(
            1.0,
            replica_count / 10,
        )

        return ParallelTemperingProfile(
            best_replica_id=best_replica_id,
            best_energy=best_energy,
            replica_count=replica_count,
            exchanges=exchanges,
            confidence=confidence,
        )
