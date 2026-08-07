"""
RNAOS meta intelligence profile engine.
"""

from __future__ import annotations

from dl.models.optimization.meta_intelligence_profile import (
    MetaIntelligenceProfile,
)


class MetaIntelligenceProfileEngine:
    """
    Generates meta optimization intelligence profiles.
    """

    def generate(
        self,
        best_algorithm: str,
        generations: int,
        best_fitness: float,
    ) -> MetaIntelligenceProfile:
        """
        Generate a meta optimization profile.
        """

        if not best_algorithm:
            raise ValueError(
                "Best algorithm cannot be empty",
            )

        if generations <= 0:
            raise ValueError(
                "Generations must be positive",
            )

        if best_fitness < 0:
            raise ValueError(
                "Best fitness cannot be negative",
            )

        confidence = min(
            1.0,
            best_fitness,
        )

        return MetaIntelligenceProfile(
            best_algorithm=best_algorithm,
            generations=generations,
            best_fitness=best_fitness,
            confidence=confidence,
        )
