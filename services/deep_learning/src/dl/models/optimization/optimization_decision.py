"""
RNAOS optimization decision models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class OptimizationDecision:
    """
    Immutable optimization decision.
    """

    strategy: str

    confidence: float

    reasoning: str
