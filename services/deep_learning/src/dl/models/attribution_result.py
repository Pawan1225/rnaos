"""
RNAOS attribution result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class AttributionResult:
    """
    Immutable explanation attribution result.
    """

    method: str

    features: tuple[str, ...]

    importance_scores: tuple[float, ...]

    confidence: float = 0.0

    metadata: tuple[str, ...] = ()
