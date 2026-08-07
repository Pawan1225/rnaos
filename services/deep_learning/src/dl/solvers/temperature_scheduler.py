"""
RNAOS temperature scheduler.
"""

from __future__ import annotations

from dl.models.optimization.temperature_state import (
    TemperatureState,
)


class TemperatureScheduler:
    """
    Controls annealing temperature decay.
    """

    def __init__(
        self,
        initial_temperature: float,
        cooling_rate: float,
    ) -> None:
        self.initial_temperature = initial_temperature

        self.cooling_rate = cooling_rate

    def temperature(
        self,
        iteration: int,
    ) -> TemperatureState:
        """
        Calculate current temperature.

        Formula:

        T = T0 * cooling_rate ^ iteration
        """

        value = self.initial_temperature * (self.cooling_rate**iteration)

        return TemperatureState(
            iteration=iteration,
            temperature=value,
        )
