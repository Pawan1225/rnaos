"""
RNAOS population resampling engine.
"""

from __future__ import annotations

from dl.models.optimization.annealing_population import (
    AnnealingPopulation,
)
from dl.models.optimization.resampling_result import (
    ResamplingResult,
)


class PopulationResamplingEngine:
    """
    Selects strongest candidates.
    """

    def resample(
        self,
        population: AnnealingPopulation,
        size: int,
    ) -> ResamplingResult:
        """
        Keep highest fitness candidates.
        """

        if size <= 0:
            raise ValueError(
                "Population size must be positive",
            )

        selected = tuple(
            sorted(
                population.candidates,
                key=lambda candidate: candidate.fitness,
                reverse=True,
            )[:size]
        )

        return ResamplingResult(
            selected=selected,
            removed_count=(len(population.candidates) - len(selected)),
            generation=population.generation + 1,
        )
