"""
RNAOS explanation configuration model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ExplanationConfiguration:
    """
    Immutable explainability settings.
    """

    method: str = "saliency"

    top_features: int = 10

    attribution_threshold: float = 0.5

    generate_visualization: bool = True

    include_attention: bool = False
