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
    Immutable optimization intelligence evaluation.
    """

    overall_score: float

    passed: bool

    recommendation: str
