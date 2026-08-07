"""
Tests for annealing population.
"""

from __future__ import annotations

from dl.models.optimization.annealing_population import (
    AnnealingPopulation,
)
from dl.models.optimization.population_candidate import (
    PopulationCandidate,
)


def test_annealing_population_creation() -> None:
    """
    Population can be created.
    """

    candidate = PopulationCandidate(
        candidate_id=1,
        state=(
            1,
            -1,
        ),
        energy=-5.0,
        fitness=0.8,
    )

    population = AnnealingPopulation(
        candidates=(candidate,),
        temperature=10.0,
        generation=1,
    )

    assert isinstance(
        population,
        AnnealingPopulation,
    )

    assert (
        len(
            population.candidates,
        )
        == 1
    )

    assert population.temperature == 10.0
    assert population.generation == 1

    assert population.candidates[0] == candidate
