"""
Tests for recombination engine.
"""

from __future__ import annotations

from dl.models.optimization.differential_vector import (
    DifferentialVector,
)
from dl.models.optimization.recombination_result import (
    RecombinationResult,
)
from dl.optimization.recombination_engine import (
    RecombinationEngine,
)


def test_recombination_engine() -> None:
    """
    Mutant vector contributes values.
    """

    target = DifferentialVector(
        vector_id=1,
        values=(
            1.0,
            1.0,
            1.0,
        ),
        fitness=0.5,
        generation=1,
    )

    mutant = DifferentialVector(
        vector_id=2,
        values=(
            2.0,
            2.0,
            2.0,
        ),
        fitness=0.7,
        generation=1,
    )

    engine = RecombinationEngine()

    result = engine.recombine(
        target,
        mutant,
        crossover_rate=1.0,
    )

    assert isinstance(
        result,
        RecombinationResult,
    )

    assert result.target_id == 1

    assert result.trial_vector.values == (
        2.0,
        2.0,
        2.0,
    )

    assert result.changed_dimensions == 3

    assert result.trial_vector.generation == 2
