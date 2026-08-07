"""
RNAOS temperature state models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class TemperatureState:
    """
    Immutable temperature state.
    """

    iteration: int

    temperature: float
