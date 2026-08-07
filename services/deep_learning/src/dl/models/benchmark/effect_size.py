"""
RNAOS effect size analysis model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class EffectSize:
    """
    Immutable effect size result.
    """

    cohens_d: float

    improvement_ratio: float

    relative_gain: float
