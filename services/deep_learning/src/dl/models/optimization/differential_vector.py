"""
RNAOS differential evolution vector model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class DifferentialVector:
    """
    Immutable continuous optimization vector.
    """

    vector_id: int

    values: tuple[float, ...]

    fitness: float

    generation: int
