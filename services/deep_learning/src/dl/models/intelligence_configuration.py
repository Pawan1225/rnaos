"""
RNAOS deep learning intelligence configuration.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class IntelligenceConfiguration:
    """
    Immutable intelligence execution settings.
    """

    model_family: str = "transformer"

    explanation_enabled: bool = True

    confidence_threshold: float = 0.5

    execution_mode: str = "standard"
