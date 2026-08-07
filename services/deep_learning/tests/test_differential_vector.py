"""
Tests for differential vector model.
"""

from __future__ import annotations

from dl.models.optimization.differential_vector import (
    DifferentialVector,
)


def test_differential_vector_creation() -> None:
    """
    Differential vector can be created.
    """

    vector = DifferentialVector(
        vector_id=1,
        values=(
            0.5,
            1.2,
            0.8,
        ),
        fitness=0.9,
        generation=1,
    )

    assert vector.vector_id == 1

    assert vector.values == (
        0.5,
        1.2,
        0.8,
    )

    assert vector.fitness == 0.9

    assert vector.generation == 1
