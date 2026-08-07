"""
Tests for crossover engine.
"""

from __future__ import annotations

from dl.models.optimization.crossover_result import (
    CrossoverResult,
)
from dl.models.optimization.genome import (
    Genome,
)
from dl.optimization.crossover_engine import (
    CrossoverEngine,
)


def test_crossover_engine() -> None:
    """
    Parent genomes create child genome.
    """

    parent_a = Genome(
        genome_id=1,
        sequence=(
            1,
            1,
            1,
            1,
        ),
        fitness=0.8,
        generation=1,
    )

    parent_b = Genome(
        genome_id=2,
        sequence=(
            0,
            0,
            0,
            0,
        ),
        fitness=0.7,
        generation=1,
    )

    engine = CrossoverEngine()

    result = engine.crossover(
        parent_a,
        parent_b,
        point=2,
    )

    assert isinstance(
        result,
        CrossoverResult,
    )

    assert result.parent_a_id == 1

    assert result.parent_b_id == 2

    assert result.child.sequence == (
        1,
        1,
        0,
        0,
    )

    assert result.child.generation == 2

    assert result.crossover_point == 2
