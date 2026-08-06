"""
RNAOS intelligence result model.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.explanation_report import (
    ExplanationReport,
)
from dl.models.prediction_result import (
    PredictionResult,
)


@dataclass(
    slots=True,
    frozen=True,
)
class IntelligenceResult:
    """
    Immutable intelligence execution result.
    """

    prediction: PredictionResult

    explanation: ExplanationReport | None

    selected_model: str

    confidence: float

    completed: bool
