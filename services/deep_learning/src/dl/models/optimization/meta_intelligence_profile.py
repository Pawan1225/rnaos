"""
RNAOS meta intelligence profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class MetaIntelligenceProfile:
    """
    Immutable meta optimization intelligence profile.
    """

    best_algorithm: str

    generations: int

    best_fitness: float

    confidence: float
