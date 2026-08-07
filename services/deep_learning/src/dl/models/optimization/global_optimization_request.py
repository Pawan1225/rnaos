"""
RNAOS global optimization request model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class GlobalOptimizationRequest:
    """
    Immutable global optimization request.
    """

    request_id: int

    problem_type: str

    complexity: float

    priority: int

    accuracy_target: float
