"""
RNAOS orchestration feature model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class OrchestrationFeature:
    """
    Immutable orchestration feature.
    """

    feature_name: str

    value: float

    category: str
