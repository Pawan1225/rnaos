"""
Crossover operators for Genetic Algorithms.
"""

from __future__ import annotations

import random


class SinglePointCrossover:
    """Single-point crossover operator."""

    @staticmethod
    def crossover(
        parent_one: list[int],
        parent_two: list[int],
    ) -> list[int]:
        """Create one child using single-point crossover."""

        if len(parent_one) != len(parent_two):
            raise ValueError("Parents must have the same length.")

        if len(parent_one) < 2:
            return parent_one.copy()

        point = random.randint(
            1,
            len(parent_one) - 1,
        )

        return parent_one[:point] + parent_two[point:]
