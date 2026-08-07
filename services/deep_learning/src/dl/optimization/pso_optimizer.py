"""
RNAOS particle swarm optimizer.
"""

from __future__ import annotations

from dl.models.optimization.pso_result import (
    PSOResult,
)
from dl.models.optimization.swarm_population import (
    SwarmPopulation,
)


class PSOOptimizer:
    """
    Executes particle swarm optimization.
    """

    def optimize(
        self,
        swarm: SwarmPopulation,
        iterations: int,
    ) -> PSOResult:
        """
        Select the best particle from the swarm.
        """

        if not swarm.particles:
            raise ValueError(
                "Swarm cannot be empty",
            )

        if iterations <= 0:
            raise ValueError(
                "Iterations must be positive",
            )

        best = max(
            swarm.particles,
            key=lambda particle: particle.fitness,
        )

        return PSOResult(
            best_particle=best,
            iterations=iterations,
            converged=True,
        )
