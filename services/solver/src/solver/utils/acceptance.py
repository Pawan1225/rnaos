"""
Acceptance criterion utilities.
"""

from __future__ import annotations

import math
import random


class MetropolisAcceptanceCriterion:
    """Metropolis acceptance criterion."""

    @staticmethod
    def accept(
        current_objective: float,
        candidate_objective: float,
        temperature: float,
    ) -> bool:
        """
        Decide whether to accept a candidate solution.

        Lower objective values are considered better because
        QUBO problems are formulated as minimization problems.
        """

        # Always accept improvements.
        if candidate_objective <= current_objective:
            return True

        # Never divide by zero.
        if temperature <= 0.0:
            return False

        delta = candidate_objective - current_objective

        probability = math.exp(-delta / temperature)

        return random.random() < probability
