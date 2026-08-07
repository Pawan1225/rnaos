"""
RNAOS population annealing profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class PopulationAnnealingProfile:
    """
    Immutable population annealing intelligence profile.
    """

    best_energy: float

    population_size: int

    generations: int

    final_temperature: float

    confidence: float
