"""
RNAOS cooling schedule interfaces.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class CoolingSchedule(ABC):
    """
    Base cooling schedule interface.
    """

    @abstractmethod
    def calculate(
        self,
        temperature: float,
        iteration: int,
    ) -> float:
        """
        Calculate next temperature.
        """

        raise NotImplementedError
