"""
RNAOS genetic mutation engine.
"""

from __future__ import annotations

import random

from dl.models.optimization.genome import (
    Genome,
)
from dl.models.optimization.mutation_result import (
    MutationResult,
)


class MutationEngine:
    """
    Performs genome mutation.
    """

    def mutate(
        self,
        genome: Genome,
        mutation_rate: float,
        seed: int = 42,
    ) -> MutationResult:
        """
        Mutate genome sequence.
        """

        if not 0.0 <= mutation_rate <= 1.0:
            raise ValueError(
                "Mutation rate must be between 0 and 1",
            )

        rng = random.Random(seed)

        sequence = list(
            genome.sequence,
        )

        mutations = 0

        for index, value in enumerate(sequence):
            if rng.random() < mutation_rate:
                sequence[index] = 1 - value
                mutations += 1

        mutated = Genome(
            genome_id=genome.genome_id,
            sequence=tuple(sequence),
            fitness=genome.fitness,
            generation=genome.generation,
        )

        return MutationResult(
            original_id=genome.genome_id,
            mutated_genome=mutated,
            mutations=mutations,
        )
