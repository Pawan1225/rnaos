"""
RNAOS annealing configuration models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class AnnealingConfiguration:
    """
    Immutable annealing configuration.
    """

    initial_temperature: float

    minimum_temperature: float

    cooling_rate: float

    iterations: int

    seed: int
