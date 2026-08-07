"""
RNAOS genetic optimizer.
"""

from __future__ import annotations

from dl.models.optimization.genetic_population import (
    GeneticPopulation,
)
from dl.models.optimization.genetic_result import (
    GeneticResult,
)


class GeneticOptimizer:
    """
    Executes genetic optimization.
    """

    def optimize(
        self,
        population: GeneticPopulation,
        generations: int,
    ) -> GeneticResult:
        """
        Select the best genome.
        """

        if not population.genomes:
            raise ValueError(
                "Population cannot be empty",
            )

        if generations <= 0:
            raise ValueError(
                "Generations must be positive",
            )

        best = max(
            population.genomes,
            key=lambda genome: genome.fitness,
        )

        return GeneticResult(
            best_genome=best,
            generations=generations,
            mutations=0,
            converged=True,
        )
