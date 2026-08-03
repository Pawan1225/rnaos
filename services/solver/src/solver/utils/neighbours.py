"""
Neighbour generation utilities.
"""

from __future__ import annotations

import random


class NeighbourGenerator:
    """Generate neighbouring binary solutions."""

    @staticmethod
    def flip_random_bit(
        solution: list[int],
    ) -> list[int]:
        """
        Return a neighbouring solution by flipping
        one randomly selected bit.
        """

        if not solution:
            raise ValueError("Solution cannot be empty.")

        neighbour = solution.copy()

        index = random.randrange(len(neighbour))

        neighbour[index] = 1 - neighbour[index]

        return neighbour
