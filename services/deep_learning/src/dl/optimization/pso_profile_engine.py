"""
RNAOS particle swarm optimization profile engine.
"""

from __future__ import annotations

from dl.models.optimization.pso_profile import (
    PSOProfile,
)


class PSOProfileEngine:
    """
    Generates PSO optimization profiles.
    """

    def generate(
        self,
        best_fitness: float,
        iterations: int,
        swarm_size: int,
    ) -> PSOProfile:
        """
        Generate PSO profile.
        """

        confidence = min(
            1.0,
            iterations / 100,
        )

        return PSOProfile(
            best_fitness=best_fitness,
            iterations=iterations,
            swarm_size=swarm_size,
            confidence=confidence,
        )
