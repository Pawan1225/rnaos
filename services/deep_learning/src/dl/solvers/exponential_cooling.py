"""
RNAOS exponential cooling schedule.
"""

from __future__ import annotations

from dl.solvers.cooling_schedule import (
    CoolingSchedule,
)


class ExponentialCooling(
    CoolingSchedule,
):
    """
    Exponential temperature decay.
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
        Apply exponential decay.
        """

        return temperature * (self.rate**iteration)
