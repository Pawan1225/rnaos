"""
RNAOS population annealing profile engine.
"""

from __future__ import annotations

from dl.models.optimization.population_annealing_profile import (
    PopulationAnnealingProfile,
)


class PopulationAnnealingProfileEngine:
    """
    Generates population annealing profiles.
    """

    def generate(
        self,
        best_energy: float,
        population_size: int,
        generations: int,
        final_temperature: float,
    ) -> PopulationAnnealingProfile:
        """
        Generate optimization profile.
        """

        confidence = min(
            1.0,
            generations / 100,
        )

        return PopulationAnnealingProfile(
            best_energy=best_energy,
            population_size=population_size,
            generations=generations,
            final_temperature=final_temperature,
            confidence=confidence,
        )
