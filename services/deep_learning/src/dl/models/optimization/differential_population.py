"""
RNAOS differential evolution population model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.differential_vector import (
    DifferentialVector,
)


@dataclass(
    slots=True,
    frozen=True,
)
class DifferentialPopulation:
    """
    Immutable differential evolution population.
    """

    vectors: tuple[DifferentialVector, ...]

    generation: int
