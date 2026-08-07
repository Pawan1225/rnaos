"""
RNAOS solver performance profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class SolverPerformanceProfile:
    """
    Immutable solver performance profile.
    """

    solver_name: str

    total_runs: int

    success_rate: float

    average_accuracy: float

    average_energy: float

    average_runtime: float
