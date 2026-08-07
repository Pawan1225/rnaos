"""
RNAOS solver configuration models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class SolverConfiguration:
    """
    Immutable solver configuration.
    """

    iterations: int

    seed: int

    initial_temperature: float

    cooling_rate: float

    convergence_threshold: float

    checkpoint_interval: int
