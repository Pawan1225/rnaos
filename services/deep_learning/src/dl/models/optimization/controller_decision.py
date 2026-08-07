"""
RNAOS adaptive controller decision model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ControllerDecision:
    """
    Immutable adaptive optimization decision.
    """

    problem_type: str

    selected_solver: str

    confidence: float

    learned: bool
