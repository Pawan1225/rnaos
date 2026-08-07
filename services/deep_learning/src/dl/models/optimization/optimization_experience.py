"""
RNAOS optimization experience model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class OptimizationExperience:
    """
    Immutable optimization experience.
    """

    experience_id: int

    solver_name: str

    problem_type: str

    fitness: float

    execution_time: float
