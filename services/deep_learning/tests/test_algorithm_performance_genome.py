"""
Tests for algorithm performance genome.
"""

from __future__ import annotations

from dl.models.optimization.algorithm_performance_genome import (
    AlgorithmPerformanceGenome,
)


def test_algorithm_performance_genome_creation() -> None:
    """
    Genome can be created.
    """

    genome = AlgorithmPerformanceGenome(
        genome_id=1,
        algorithm_name="genetic",
        genes=(
            0.10,
            100.0,
            0.80,
        ),
        fitness=0.95,
        generation=1,
    )

    assert genome.genome_id == 1

    assert genome.algorithm_name == "genetic"

    assert genome.genes == (
        0.10,
        100.0,
        0.80,
    )

    assert genome.fitness == 0.95

    assert genome.generation == 1
