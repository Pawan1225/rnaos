"""
RNAOS population resampling result model.
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
class ResamplingResult:
    """
    Immutable population resampling result.
    """

    selected: tuple[PopulationCandidate, ...]

    removed_count: int

    generation: int
