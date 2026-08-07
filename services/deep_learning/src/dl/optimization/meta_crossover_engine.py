"""
RNAOS meta crossover engine.
"""

from __future__ import annotations

from dl.models.optimization.algorithm_performance_genome import (
    AlgorithmPerformanceGenome,
)
from dl.models.optimization.meta_crossover_result import (
    MetaCrossoverResult,
)


class MetaCrossoverEngine:
    """
    Performs deterministic crossover between
    two algorithm genomes.
    """

    def crossover(
        self,
        parent_one: AlgorithmPerformanceGenome,
        parent_two: AlgorithmPerformanceGenome,
    ) -> MetaCrossoverResult:
        """
        Create offspring genome.
        """

        if len(parent_one.genes) != len(
            parent_two.genes,
        ):
            raise ValueError(
                "Genome lengths must match",
            )

        midpoint = (
            len(
                parent_one.genes,
            )
            // 2
        )

        offspring_genes = parent_one.genes[:midpoint] + parent_two.genes[midpoint:]

        offspring = AlgorithmPerformanceGenome(
            genome_id=max(
                parent_one.genome_id,
                parent_two.genome_id,
            )
            + 1,
            algorithm_name=parent_one.algorithm_name,
            genes=offspring_genes,
            fitness=max(
                parent_one.fitness,
                parent_two.fitness,
            ),
            generation=max(
                parent_one.generation,
                parent_two.generation,
            )
            + 1,
        )

        return MetaCrossoverResult(
            parent_one=parent_one,
            parent_two=parent_two,
            offspring=offspring,
            crossover_point=midpoint,
        )
