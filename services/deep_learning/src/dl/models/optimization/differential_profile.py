"""
RNAOS differential evolution profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class DifferentialProfile:
    """
    Immutable differential evolution profile.
    """

    best_fitness: float

    generations: int

    vector_dimension: int

    confidence: float
