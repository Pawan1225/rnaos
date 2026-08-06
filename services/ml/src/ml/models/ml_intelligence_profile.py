"""
RNAOS machine learning intelligence profile.
"""

from __future__ import annotations

from dataclasses import dataclass

from ml.models.model_evaluation import (
    ModelEvaluation,
)
from ml.models.prediction_result import (
    PredictionResult,
)


@dataclass(slots=True, frozen=True)
class MLIntelligenceProfile:
    """
    Immutable machine learning intelligence output.

    Represents the final result produced by
    the ML Intelligence Engine pipeline.
    """

    experiment_id: str

    dataset_version: str

    selected_features: tuple[str, ...]

    model_name: str

    prediction_result: PredictionResult

    evaluation_result: ModelEvaluation

    registered_model_id: str
