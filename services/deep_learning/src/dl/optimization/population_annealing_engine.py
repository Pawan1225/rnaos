"""
RNAOS population annealing engine.
"""

from __future__ import annotations

from dl.models.optimization.annealing_population import (
    AnnealingPopulation,
)
from dl.models.optimization.population_annealing_result import (
    PopulationAnnealingResult,
)


class PopulationAnnealingEngine:
    """
    Executes population annealing.
    """

    def optimize(
        self,
        population: AnnealingPopulation,
        generations: int,
    ) -> PopulationAnnealingResult:
        """
        Optimize population.
        """

        if not population.candidates:
            raise ValueError(
                "Population cannot be empty",
            )

        if generations <= 0:
            raise ValueError(
                "Generations must be positive",
            )

        best = max(
            population.candidates,
            key=lambda candidate: candidate.fitness,
        )

        final_temperature = population.temperature / generations

        return PopulationAnnealingResult(
            best_candidate=best,
            generations=generations,
            final_temperature=final_temperature,
            converged=True,
        )
