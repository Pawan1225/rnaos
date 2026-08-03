"""
Configuration for Simulated Annealing.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class AnnealingConfig:
    """Configuration parameters for Simulated Annealing."""

    max_iterations: int = 1_000

    initial_temperature: float = 100.0

    cooling_rate: float = 0.995

    minimum_temperature: float = 1e-3
