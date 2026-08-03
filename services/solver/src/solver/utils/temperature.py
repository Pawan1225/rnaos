"""
Temperature schedule utilities.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class ExponentialCoolingSchedule:
    """
    Exponential cooling schedule.

    Temperature is updated as:

        T = T * cooling_rate
    """

    initial_temperature: float = 100.0

    cooling_rate: float = 0.995

    minimum_temperature: float = 1e-3

    def temperature(
        self,
        iteration: int,
    ) -> float:
        """
        Return the temperature for a given iteration.
        """

        value = self.initial_temperature * (self.cooling_rate**iteration)

        return max(
            value,
            self.minimum_temperature,
        )
