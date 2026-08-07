"""
RNAOS acceptance probability engine.
"""

from __future__ import annotations

import math
import random

from dl.models.optimization.acceptance_result import (
    AcceptanceResult,
)


class AcceptanceProbabilityEngine:
    """
    Calculates annealing acceptance.
    """

    def __init__(
        self,
        seed: int = 42,
    ) -> None:
        random.seed(
            seed,
        )

    def calculate(
        self,
        current_energy: float,
        new_energy: float,
        temperature: float,
    ) -> AcceptanceResult:
        """
        Determine whether to accept move.
        """

        if temperature <= 0:
            raise ValueError(
                "Temperature must be positive",
            )

        delta = new_energy - current_energy

        if delta <= 0:
            return AcceptanceResult(
                probability=1.0,
                accepted=True,
            )

        probability = math.exp(
            -delta / temperature,
        )

        return AcceptanceResult(
            probability=probability,
            accepted=(random.random() < probability),
        )
