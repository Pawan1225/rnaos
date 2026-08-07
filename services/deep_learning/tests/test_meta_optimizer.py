"""
Tests for meta optimizer.
"""

from __future__ import annotations

from dl.models.optimization.algorithm_performance_genome import (
    AlgorithmPerformanceGenome,
)
from dl.models.optimization.meta_optimizer_result import (
    MetaOptimizerResult,
)
from dl.optimization.meta_optimizer import (
    MetaOptimizer,
)


def test_meta_optimizer() -> None:
    """
    Best genome is selected.
    """

    genomes = (
        AlgorithmPerformanceGenome(
            genome_id=1,
            algorithm_name="genetic",
            genes=(
                0.10,
                100.0,
            ),
            fitness=0.80,
            generation=1,
        ),
        AlgorithmPerformanceGenome(
            genome_id=2,
            algorithm_name="pso",
            genes=(
                0.20,
                200.0,
            ),
            fitness=0.95,
            generation=1,
        ),
    )

    optimizer = MetaOptimizer()

    result = optimizer.optimize(
        genomes=genomes,
        generations=10,
    )

    assert isinstance(
        result,
        MetaOptimizerResult,
    )

    assert result.best_genome.algorithm_name == "pso"

    assert result.best_genome.genome_id == 2

    assert result.generations == 10

    assert result.improved is True
