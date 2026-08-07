"""
Tests for genome model.
"""

from __future__ import annotations

from dl.models.optimization.genome import (
    Genome,
)


def test_genome_creation() -> None:
    """
    Genome can be created.
    """

    genome = Genome(
        genome_id=1,
        sequence=(
            1,
            0,
            1,
            1,
        ),
        fitness=0.9,
        generation=1,
    )

    assert genome.genome_id == 1

    assert genome.sequence == (
        1,
        0,
        1,
        1,
    )

    assert genome.fitness == 0.9

    assert genome.generation == 1
