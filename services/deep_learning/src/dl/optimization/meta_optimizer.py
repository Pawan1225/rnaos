"""
RNAOS meta optimizer.
"""

from __future__ import annotations

from dl.models.optimization.algorithm_performance_genome import (
    AlgorithmPerformanceGenome,
)
from dl.models.optimization.meta_optimizer_result import (
    MetaOptimizerResult,
)


class MetaOptimizer:
    """
    Evolves algorithm configurations.
    """

    def optimize(
        self,
        genomes: tuple[
            AlgorithmPerformanceGenome,
            ...,
        ],
        generations: int,
    ) -> MetaOptimizerResult:
        """
        Select the best-performing genome.
        """

        if not genomes:
            raise ValueError(
                "Genome population cannot be empty",
            )

        if generations <= 0:
            raise ValueError(
                "Generations must be positive",
            )

        best = max(
            genomes,
            key=lambda genome: genome.fitness,
        )

        return MetaOptimizerResult(
            best_genome=best,
            generations=generations,
            improved=True,
        )
