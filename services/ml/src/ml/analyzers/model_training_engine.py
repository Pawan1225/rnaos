"""
RNAOS model training engine.
"""

from __future__ import annotations

import time

from ml.models.ml_dataset import (
    MLDataset,
)
from ml.models.trained_model import (
    TrainedModel,
)
from ml.models.training_configuration import (
    TrainingConfiguration,
)
from ml.utils.cross_validation import (
    evaluate_model,
)
from ml.utils.training_utils import (
    create_model,
    train_model,
)


class ModelTrainingEngine:
    """
    Train a single machine learning model.

    Complexity
    ----------
    Time Complexity:
        Dominated by model fitting and cross-validation.
    """

    def analyze(
        self,
        dataset: MLDataset,
        configuration: TrainingConfiguration,
    ) -> TrainedModel:
        """
        Train and evaluate a single machine learning model.
        """
        model_name = configuration.model_name

        model = create_model(
            model_name,
        )

        start_time = time.perf_counter()

        trained = train_model(
            model=model,
            features=dataset.features,
            targets=dataset.targets,
        )

        training_time = time.perf_counter() - start_time

        score = evaluate_model(
            model=trained,
            features=dataset.features,
            targets=dataset.targets,
            folds=configuration.cross_validation_folds,
        )

        return TrainedModel(
            model_name=model_name,
            estimator=trained,
            score=score,
            training_time=training_time,
            feature_count=dataset.feature_count,
            sample_count=dataset.sample_count,
        )
