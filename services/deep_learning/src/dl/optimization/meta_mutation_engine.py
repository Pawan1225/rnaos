"""
RNAOS meta mutation engine.
"""

from __future__ import annotations

from dl.models.optimization.algorithm_performance_genome import (
    AlgorithmPerformanceGenome,
)
from dl.models.optimization.meta_mutation_result import (
    MetaMutationResult,
)


class MetaMutationEngine:
    """
    Evolves algorithm genomes through mutation.
    """

    def mutate(
        self,
        genome: AlgorithmPerformanceGenome,
        mutation_rate: float,
    ) -> MetaMutationResult:
        """
        Mutate genome parameters.
        """

        if not 0.0 <= mutation_rate <= 1.0:
            raise ValueError(
                "Mutation rate must be between 0 and 1",
            )

        mutated_genes = tuple(gene + mutation_rate for gene in genome.genes)

        mutated = AlgorithmPerformanceGenome(
            genome_id=genome.genome_id,
            algorithm_name=genome.algorithm_name,
            genes=mutated_genes,
            fitness=genome.fitness,
            generation=genome.generation + 1,
        )

        return MetaMutationResult(
            original=genome,
            mutated=mutated,
            mutation_rate=mutation_rate,
        )
