"""
RNAOS genetic optimization profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class GeneticProfile:
    """
    Immutable genetic optimization profile.
    """

    best_fitness: float

    generations: int

    mutations: int

    confidence: float
