"""
RNAOS AutoML result model.
"""

from __future__ import annotations

from dataclasses import dataclass

from ml.models.trained_model import (
    TrainedModel,
)
from ml.models.training_configuration import (
    TrainingConfiguration,
)


@dataclass(slots=True, frozen=True)
class AutoMLResult:
    """
    Immutable AutoML training result.
    """

    trained_models: tuple[TrainedModel, ...]

    best_model: TrainedModel

    ranking: tuple[str, ...]

    training_configuration: TrainingConfiguration

    total_training_time: float

    dataset_version: str

    experiment_id: str

    @property
    def model_count(
        self,
    ) -> int:
        """
        Number of trained models.
        """
        return len(
            self.trained_models,
        )

    @property
    def best_model_name(
        self,
    ) -> str:
        """
        Name of the best-performing model.
        """
        return self.best_model.model_name

    @property
    def best_score(
        self,
    ) -> float:
        """
        Best evaluation score.
        """
        return self.best_model.score

    @property
    def is_empty(
        self,
    ) -> bool:
        """
        Whether any models were trained.
        """
        return self.model_count == 0
