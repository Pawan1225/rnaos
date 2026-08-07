"""
Tests for genetic population model.
"""

from __future__ import annotations

from dl.models.optimization.genetic_population import (
    GeneticPopulation,
)
from dl.models.optimization.genome import (
    Genome,
)


def test_genetic_population_creation() -> None:
    """
    Population can be created.
    """

    genome = Genome(
        genome_id=1,
        sequence=(
            1,
            0,
            1,
        ),
        fitness=0.8,
        generation=1,
    )

    population = GeneticPopulation(
        genomes=(genome,),
        generation=1,
    )

    assert isinstance(
        population,
        GeneticPopulation,
    )

    assert (
        len(
            population.genomes,
        )
        == 1
    )

    assert population.generation == 1

    assert population.genomes[0] == genome
