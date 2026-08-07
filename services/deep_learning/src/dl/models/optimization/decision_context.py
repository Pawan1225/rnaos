"""
RNAOS adaptive decision context model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class DecisionContext:
    """
    Immutable optimization decision context.
    """

    problem_type: str

    complexity: float

    accuracy_requirement: float

    resource_level: float
