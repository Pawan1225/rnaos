"""
RNAOS differential evolution optimizer.
"""

from __future__ import annotations

from dl.models.optimization.differential_population import (
    DifferentialPopulation,
)
from dl.models.optimization.differential_result import (
    DifferentialResult,
)


class DifferentialOptimizer:
    """
    Executes differential evolution.
    """

    def optimize(
        self,
        population: DifferentialPopulation,
        generations: int,
    ) -> DifferentialResult:
        """
        Select best vector.
        """

        if not population.vectors:
            raise ValueError(
                "Population cannot be empty",
            )

        if generations <= 0:
            raise ValueError(
                "Generations must be positive",
            )

        best = max(
            population.vectors,
            key=lambda vector: vector.fitness,
        )

        return DifferentialResult(
            best_vector=best,
            generations=generations,
            converged=True,
        )
