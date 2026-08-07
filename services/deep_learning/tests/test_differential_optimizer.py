"""
Tests for differential optimizer.
"""

from __future__ import annotations

from dl.models.optimization.differential_population import (
    DifferentialPopulation,
)
from dl.models.optimization.differential_result import (
    DifferentialResult,
)
from dl.models.optimization.differential_vector import (
    DifferentialVector,
)
from dl.optimization.differential_optimizer import (
    DifferentialOptimizer,
)


def test_differential_optimizer() -> None:
    """
    Best vector is selected.
    """

    population = DifferentialPopulation(
        vectors=(
            DifferentialVector(
                vector_id=1,
                values=(
                    0.1,
                    0.2,
                ),
                fitness=0.5,
                generation=1,
            ),
            DifferentialVector(
                vector_id=2,
                values=(
                    0.9,
                    1.2,
                ),
                fitness=0.95,
                generation=1,
            ),
        ),
        generation=1,
    )

    optimizer = DifferentialOptimizer()

    result = optimizer.optimize(
        population,
        generations=20,
    )

    assert isinstance(
        result,
        DifferentialResult,
    )

    assert result.best_vector.vector_id == 2

    assert result.generations == 20

    assert result.converged is True
