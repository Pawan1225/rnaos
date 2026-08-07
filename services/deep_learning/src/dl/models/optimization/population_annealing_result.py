"""
RNAOS population annealing result model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.population_candidate import (
    PopulationCandidate,
)


@dataclass(
    slots=True,
    frozen=True,
)
class PopulationAnnealingResult:
    """
    Immutable population annealing result.
    """

    best_candidate: PopulationCandidate

    generations: int

    final_temperature: float

    converged: bool
