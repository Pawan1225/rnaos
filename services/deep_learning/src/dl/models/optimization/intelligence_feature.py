"""
RNAOS intelligence feature model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class IntelligenceFeature:
    """
    Immutable optimization intelligence feature.
    """

    feature_name: str

    value: float

    category: str
