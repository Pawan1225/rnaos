"""
RNAOS local search profile engine.
"""

from __future__ import annotations

from dl.models.optimization.local_search_profile import (
    LocalSearchProfile,
)


class LocalSearchProfileEngine:
    """
    Generates local search optimization profiles.
    """

    def generate(
        self,
        best_energy: float,
        iterations: int,
        search_strategy: str,
    ) -> LocalSearchProfile:
        """
        Generate local search profile.
        """

        if iterations <= 0:
            raise ValueError(
                "Iterations must be positive",
            )

        if not search_strategy:
            raise ValueError(
                "Search strategy cannot be empty",
            )

        confidence = min(
            1.0,
            iterations / 100,
        )

        return LocalSearchProfile(
            best_energy=best_energy,
            iterations=iterations,
            search_strategy=search_strategy,
            confidence=confidence,
        )
