"""
RNAOS unified optimization problem model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.constraint import (
    Constraint,
)
from dl.models.optimization.optimization_variable import (
    OptimizationVariable,
)


@dataclass(
    slots=True,
    frozen=True,
)
class OptimizationProblem:
    """
    Complete optimization problem definition.
    """

    name: str

    variables: tuple[OptimizationVariable, ...]

    constraints: tuple[Constraint, ...]

    objective: str
