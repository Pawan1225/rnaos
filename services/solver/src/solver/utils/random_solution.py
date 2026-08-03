"""
Random solution generation utilities.
"""

from __future__ import annotations

import random

from optimization.models.optimization_problem import QUBOProblem


class RandomSolutionGenerator:
    """Generate random binary solutions."""

    @staticmethod
    def generate(
        problem: QUBOProblem,
    ) -> list[int]:
        """
        Generate a random binary solution.

        Each variable is independently assigned
        either 0 or 1 with equal probability.
        """

        return [random.randint(0, 1) for _ in range(problem.size)]
