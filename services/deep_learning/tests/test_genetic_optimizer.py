"""
Tests for genetic optimizer.
"""

from __future__ import annotations

from dl.models.optimization.genetic_population import (
    GeneticPopulation,
)
from dl.models.optimization.genetic_result import (
    GeneticResult,
)
from dl.models.optimization.genome import (
    Genome,
)
from dl.optimization.genetic_optimizer import (
    GeneticOptimizer,
)


def test_genetic_optimizer() -> None:
    """
    Best genome is selected.
    """

    population = GeneticPopulation(
        genomes=(
            Genome(
                genome_id=1,
                sequence=(
                    1,
                    0,
                ),
                fitness=0.5,
                generation=1,
            ),
            Genome(
                genome_id=2,
                sequence=(
                    1,
                    1,
                ),
                fitness=0.9,
                generation=1,
            ),
        ),
        generation=1,
    )

    optimizer = GeneticOptimizer()

    result = optimizer.optimize(
        population,
        generations=10,
    )

    assert isinstance(
        result,
        GeneticResult,
    )

    assert result.best_genome.genome_id == 2

    assert result.generations == 10

    assert result.mutations == 0

    assert result.converged is True
