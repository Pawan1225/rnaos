"""
RNAOS annealing intelligence profile models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class AnnealingProfile:
    """
    Immutable annealing intelligence profile.
    """

    algorithm: str

    initial_temperature: float

    cooling_strategy: str

    acceptance_strategy: str

    restart_enabled: bool

    convergence_threshold: float
