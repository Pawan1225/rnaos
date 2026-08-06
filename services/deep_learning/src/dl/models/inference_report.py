"""
RNAOS inference report model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.prediction_result import (
    PredictionResult,
)


@dataclass(
    slots=True,
    frozen=True,
)
class InferenceReport:
    """
    Immutable inference execution report.
    """

    prediction: PredictionResult

    confidence: float

    completed: bool
