"""
RNAOS prediction result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class PredictionResult:
    """
    Immutable inference prediction output.
    """

    prediction_task: str

    value: float

    model_version: str = "v1"

    confidence: float = 0.0

    metadata: tuple[str, ...] = ()
