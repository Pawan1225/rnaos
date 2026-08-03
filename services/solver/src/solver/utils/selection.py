"""
Selection operators for Genetic Algorithms.
"""

from __future__ import annotations

import random
from collections.abc import Callable


class TournamentSelection:
    """Tournament selection operator."""

    @staticmethod
    def select(
        population: list[list[int]],
        score: Callable[[list[int]], float],
        tournament_size: int = 3,
    ) -> list[int]:
        """Select one parent using tournament selection."""

        contestants = random.sample(
            population,
            min(
                tournament_size,
                len(population),
            ),
        )

        return min(
            contestants,
            key=score,
        ).copy()
