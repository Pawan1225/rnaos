"""
RNAOS model feedback model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ModelFeedback:
    """
    Immutable model feedback result.
    """

    model_id: str

    prediction_error: float

    confidence_score: float

    drift_detected: bool

    retraining_required: bool

    recommendation: str
