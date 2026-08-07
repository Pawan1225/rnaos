"""
RNAOS final intelligence profile model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class FinalIntelligenceProfile:
    """
    Immutable final intelligence profile.
    """

    system_name: str

    version: str

    active_solvers: tuple[str, ...]

    intelligence_score: float

    validation_status: str
