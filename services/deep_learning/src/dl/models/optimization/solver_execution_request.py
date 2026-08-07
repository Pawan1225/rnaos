"""
RNAOS solver execution request model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class SolverExecutionRequest:
    """
    Immutable solver execution request.
    """

    request_id: int

    problem_type: str

    strategy_name: str

    priority: int
