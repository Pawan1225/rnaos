"""
Tests for differential mutation engine.
"""

from __future__ import annotations

from dl.models.optimization.differential_vector import (
    DifferentialVector,
)
from dl.models.optimization.mutation_vector_result import (
    MutationVectorResult,
)
from dl.optimization.differential_mutation_engine import (
    DifferentialMutationEngine,
)


def test_differential_mutation() -> None:
    """
    Differential mutation creates mutant vector.
    """

    base = DifferentialVector(
        vector_id=1,
        values=(
            1.0,
            2.0,
        ),
        fitness=0.5,
        generation=1,
    )

    vector_b = DifferentialVector(
        vector_id=2,
        values=(
            3.0,
            4.0,
        ),
        fitness=0.6,
        generation=1,
    )

    vector_c = DifferentialVector(
        vector_id=3,
        values=(
            1.0,
            1.0,
        ),
        fitness=0.4,
        generation=1,
    )

    engine = DifferentialMutationEngine()

    result = engine.mutate(
        base,
        vector_b,
        vector_c,
        factor=0.5,
    )

    assert isinstance(
        result,
        MutationVectorResult,
    )

    assert result.base_vector_id == 1

    assert result.mutant_vector.values == (
        2.0,
        3.5,
    )

    assert result.mutant_vector.generation == 2

    assert result.mutant_vector.fitness == 0.0
