"""
Tests for meta mutation engine.
"""

from __future__ import annotations

from dl.models.optimization.algorithm_performance_genome import (
    AlgorithmPerformanceGenome,
)
from dl.models.optimization.meta_mutation_result import (
    MetaMutationResult,
)
from dl.optimization.meta_mutation_engine import (
    MetaMutationEngine,
)


def test_meta_mutation() -> None:
    """
    Genome mutation is performed.
    """

    genome = AlgorithmPerformanceGenome(
        genome_id=1,
        algorithm_name="genetic",
        genes=(
            0.1,
            100.0,
            0.8,
        ),
        fitness=0.95,
        generation=1,
    )

    engine = MetaMutationEngine()

    result = engine.mutate(
        genome,
        mutation_rate=0.1,
    )

    assert isinstance(
        result,
        MetaMutationResult,
    )

    assert result.original == genome

    assert result.mutated.genome_id == 1

    assert result.mutated.generation == 2

    assert result.mutated.genes == (
        0.2,
        100.1,
        0.9,
    )

    assert result.mutation_rate == 0.1
