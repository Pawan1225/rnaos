"""
RNAOS base pair reward models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class BasePairReward:
    """
    Immutable RNA base pairing reward.
    """

    pair_type: str

    energy: float
