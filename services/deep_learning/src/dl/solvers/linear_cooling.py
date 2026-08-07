"""
RNAOS linear cooling schedule.
"""

from __future__ import annotations

from dl.solvers.cooling_schedule import (
    CoolingSchedule,
)


class LinearCooling(
    CoolingSchedule,
):
    """
    Linear temperature reduction.
    """

    def __init__(
        self,
        rate: float,
    ) -> None:
        self.rate = rate

    def calculate(
        self,
        temperature: float,
        iteration: int,
    ) -> float:
        """
        Reduce temperature linearly.
        """

        return max(
            temperature - (self.rate * iteration),
            0.0,
        )
