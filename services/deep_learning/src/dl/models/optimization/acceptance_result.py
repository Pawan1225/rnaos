"""
RNAOS acceptance probability models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class AcceptanceResult:
    """
    Immutable acceptance decision.
    """

    probability: float

    accepted: bool
