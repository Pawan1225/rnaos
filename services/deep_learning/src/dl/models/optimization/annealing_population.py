"""
RNAOS annealing population model.
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
class AnnealingPopulation:
    """
    Immutable annealing population.
    """

    candidates: tuple[PopulationCandidate, ...]

    temperature: float

    generation: int
