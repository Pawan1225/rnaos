"""
RNAOS genetic optimization profile engine.
"""

from __future__ import annotations

from dl.models.optimization.genetic_profile import (
    GeneticProfile,
)


class GeneticProfileEngine:
    """
    Generates genetic optimization profiles.
    """

    def generate(
        self,
        best_fitness: float,
        generations: int,
        mutations: int,
    ) -> GeneticProfile:
        """
        Generate profile.
        """

        confidence = min(
            1.0,
            generations / 100,
        )

        return GeneticProfile(
            best_fitness=best_fitness,
            generations=generations,
            mutations=mutations,
            confidence=confidence,
        )
