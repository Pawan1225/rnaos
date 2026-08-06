"""
RNAOS registered machine learning model.
"""

from __future__ import annotations

from dataclasses import dataclass

from ml.models.model_evaluation import (
    ModelEvaluation,
)
from ml.models.model_metadata import (
    ModelMetadata,
)
from ml.models.trained_model import (
    TrainedModel,
)


@dataclass(slots=True, frozen=True)
class RegisteredModel:
    """
    Immutable registered model container.
    """

    metadata: ModelMetadata

    trained_model: TrainedModel

    evaluation: ModelEvaluation
