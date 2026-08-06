"""
RNAOS intelligence evaluation model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class IntelligenceEvaluation:
    """
    Immutable intelligence evaluation result.
    """

    error: float

    absolute_error: float

    passed_threshold: bool
