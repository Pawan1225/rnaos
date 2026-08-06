"""
RNAOS AutoML engine.
"""

from __future__ import annotations

import time

from ml.analyzers.model_training_engine import (
    ModelTrainingEngine,
)
from ml.models.automl_configuration import (
    AutoMLConfiguration,
)
from ml.models.automl_result import (
    AutoMLResult,
)
from ml.models.ml_dataset import (
    MLDataset,
)
from ml.models.trained_model import (
    TrainedModel,
)
from ml.models.training_configuration import (
    TrainingConfiguration,
)
from ml.utils.experiment_utils import (
    generate_experiment_id,
)


class AutoMLEngine:
    """
    Train and rank multiple machine learning models.
    """

    def __init__(self) -> None:
        """Initialize the AutoML engine."""

        self._training_engine = ModelTrainingEngine()

    def analyze(
        self,
        dataset: MLDataset,
        configuration: AutoMLConfiguration,
    ) -> AutoMLResult:
        """
        Execute the AutoML pipeline.
        """

        trained_models: list[TrainedModel] = []

        start_time = time.perf_counter()

        for model_name in configuration.model_names:
            training_configuration = TrainingConfiguration(
                model_name=model_name,
                cross_validation_folds=configuration.cross_validation_folds,
                random_seed=configuration.random_seed,
                shuffle=configuration.shuffle,
            )

            trained_model = self._training_engine.analyze(
                dataset=dataset,
                configuration=training_configuration,
            )

            trained_models.append(
                trained_model,
            )

        total_training_time = time.perf_counter() - start_time

        trained_models.sort(
            key=lambda model: model.score,
            reverse=True,
        )

        best_model = trained_models[0]

        return AutoMLResult(
            trained_models=tuple(
                trained_models,
            ),
            best_model=best_model,
            ranking=tuple(model.model_name for model in trained_models),
            training_configuration=configuration,
            total_training_time=total_training_time,
            dataset_version=dataset.dataset_version,
            experiment_id=generate_experiment_id(
                dataset.dataset_version,
            ),
        )
