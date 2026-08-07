"""
Tests for mutation engine.
"""

from __future__ import annotations

from dl.models.optimization.genome import (
    Genome,
)
from dl.models.optimization.mutation_result import (
    MutationResult,
)
from dl.optimization.mutation_engine import (
    MutationEngine,
)


def test_mutation_engine() -> None:
    """
    Genome mutation works.
    """

    genome = Genome(
        genome_id=1,
        sequence=(
            1,
            0,
            1,
            0,
        ),
        fitness=0.8,
        generation=1,
    )

    engine = MutationEngine()

    result = engine.mutate(
        genome,
        mutation_rate=1.0,
    )

    assert isinstance(
        result,
        MutationResult,
    )

    assert result.original_id == 1

    assert result.mutations == 4

    assert result.mutated_genome.sequence == (
        0,
        1,
        0,
        1,
    )

    assert result.mutated_genome.generation == 1

    assert result.mutated_genome.fitness == 0.8
