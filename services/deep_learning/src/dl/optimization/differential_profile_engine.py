"""
RNAOS differential evolution profile engine.
"""

from __future__ import annotations

from dl.models.optimization.differential_profile import (
    DifferentialProfile,
)


class DifferentialProfileEngine:
    """
    Generates differential evolution profiles.
    """

    def generate(
        self,
        best_fitness: float,
        generations: int,
        vector_dimension: int,
    ) -> DifferentialProfile:
        """
        Generate optimization profile.
        """

        confidence = min(
            1.0,
            generations / 100,
        )

        return DifferentialProfile(
            best_fitness=best_fitness,
            generations=generations,
            vector_dimension=vector_dimension,
            confidence=confidence,
        )
