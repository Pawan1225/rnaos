"""
Tests for meta crossover engine.
"""

from __future__ import annotations

from dl.models.optimization.algorithm_performance_genome import (
    AlgorithmPerformanceGenome,
)
from dl.models.optimization.meta_crossover_result import (
    MetaCrossoverResult,
)
from dl.optimization.meta_crossover_engine import (
    MetaCrossoverEngine,
)


def test_meta_crossover() -> None:
    """
    Meta crossover produces offspring.
    """

    parent_one = AlgorithmPerformanceGenome(
        genome_id=1,
        algorithm_name="genetic",
        genes=(
            0.10,
            100.0,
            0.80,
            0.40,
        ),
        fitness=0.90,
        generation=1,
    )

    parent_two = AlgorithmPerformanceGenome(
        genome_id=2,
        algorithm_name="genetic",
        genes=(
            0.20,
            120.0,
            0.90,
            0.60,
        ),
        fitness=0.95,
        generation=1,
    )

    engine = MetaCrossoverEngine()

    result = engine.crossover(
        parent_one,
        parent_two,
    )

    assert isinstance(
        result,
        MetaCrossoverResult,
    )

    assert result.parent_one == parent_one

    assert result.parent_two == parent_two

    assert result.offspring.genes == (
        0.10,
        100.0,
        0.90,
        0.60,
    )

    assert result.offspring.genome_id == 3

    assert result.offspring.generation == 2

    assert result.offspring.fitness == 0.95

    assert result.crossover_point == 2
