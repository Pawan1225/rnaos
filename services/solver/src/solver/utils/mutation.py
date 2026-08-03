"""
Mutation operators for Genetic Algorithms.
"""

from __future__ import annotations

import random


class BitFlipMutation:
    """Bit-flip mutation operator."""

    @staticmethod
    def mutate(
        solution: list[int],
        mutation_rate: float,
    ) -> list[int]:
        """
        Return a mutated copy of the solution.
        """

        mutated = solution.copy()

        for index in range(len(mutated)):
            if random.random() < mutation_rate:
                mutated[index] ^= 1

        return mutated
