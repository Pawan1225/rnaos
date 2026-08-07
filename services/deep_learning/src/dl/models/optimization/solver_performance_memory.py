"""
RNAOS solver performance memory model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.optimization_experience import (
    OptimizationExperience,
)


@dataclass(
    slots=True,
    frozen=True,
)
class SolverPerformanceMemory:
    """
    Immutable solver performance memory.
    """

    experiences: tuple[OptimizationExperience, ...]
