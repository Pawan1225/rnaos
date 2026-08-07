"""
Tests for differential population model.
"""

from __future__ import annotations

from dl.models.optimization.differential_population import (
    DifferentialPopulation,
)
from dl.models.optimization.differential_vector import (
    DifferentialVector,
)


def test_differential_population_creation() -> None:
    """
    Population can be created.
    """

    vector = DifferentialVector(
        vector_id=1,
        values=(
            0.5,
            1.0,
        ),
        fitness=0.8,
        generation=1,
    )

    population = DifferentialPopulation(
        vectors=(vector,),
        generation=1,
    )

    assert isinstance(
        population,
        DifferentialPopulation,
    )

    assert (
        len(
            population.vectors,
        )
        == 1
    )

    assert population.generation == 1

    assert population.vectors[0] == vector
