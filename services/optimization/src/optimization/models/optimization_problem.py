"""
Optimization Problem Model

Defines the solver-independent optimization representation used
throughout RNAOS.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class VariableType(StrEnum):
    """Supported optimization variable types."""

    BINARY = "binary"
    INTEGER = "integer"
    CONTINUOUS = "continuous"


class ObjectiveSense(StrEnum):
    """Supported optimization objective senses."""

    MINIMIZE = "minimize"
    MAXIMIZE = "maximize"


@dataclass(slots=True)
class DecisionVariable:
    """Represents an optimization decision variable."""

    name: str
    variable_type: VariableType
    lower_bound: float = 0.0
    upper_bound: float = 1.0


@dataclass(slots=True)
class ObjectiveFunction:
    """Represents an optimization objective."""

    expression: str
    sense: ObjectiveSense = ObjectiveSense.MINIMIZE


@dataclass(slots=True)
class Constraint:
    """Represents an optimization constraint."""

    name: str
    expression: str
    enabled: bool = True


@dataclass(slots=True)
class OptimizationMetadata:
    """Metadata describing an optimization problem."""

    solver_hint: str
    complexity_score: float
    tags: list[str] = field(default_factory=list)
    extra: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class OptimizationProblem:
    """Solver-independent optimization problem."""

    variables: list[DecisionVariable]
    objective: ObjectiveFunction
    constraints: list[Constraint]
    metadata: OptimizationMetadata

    @property
    def variable_count(self) -> int:
        """Return the number of decision variables."""
        return len(self.variables)

    @property
    def constraint_count(self) -> int:
        """Return the number of constraints."""
        return len(self.constraints)


@dataclass(slots=True)
class QUBOProblem:
    """Quadratic Unconstrained Binary Optimization problem."""

    matrix: list[list[float]]
    variable_names: list[str]

    @property
    def size(self) -> int:
        """Return the number of optimization variables."""
        return len(self.variable_names)


@dataclass(slots=True)
class OptimizationProfile:
    """Complete optimization output."""

    problem: OptimizationProblem
    qubo: QUBOProblem
