"""
RNAOS genetic crossover engine.
"""

from __future__ import annotations

from dl.models.optimization.crossover_result import (
    CrossoverResult,
)
from dl.models.optimization.genome import (
    Genome,
)


class CrossoverEngine:
    """
    Combines two genomes.
    """

    def crossover(
        self,
        parent_a: Genome,
        parent_b: Genome,
        point: int,
    ) -> CrossoverResult:
        """
        Single-point crossover.
        """

        if len(parent_a.sequence) != len(
            parent_b.sequence,
        ):
            raise ValueError(
                "Genome lengths must match",
            )

        if point <= 0 or point >= len(
            parent_a.sequence,
        ):
            raise ValueError(
                "Invalid crossover point",
            )

        child_sequence = parent_a.sequence[:point] + parent_b.sequence[point:]

        child = Genome(
            genome_id=-1,
            sequence=child_sequence,
            fitness=0.0,
            generation=max(
                parent_a.generation,
                parent_b.generation,
            )
            + 1,
        )

        return CrossoverResult(
            parent_a_id=parent_a.genome_id,
            parent_b_id=parent_b.genome_id,
            child=child,
            crossover_point=point,
        )
