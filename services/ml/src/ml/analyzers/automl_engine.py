"""
RNAOS AutoML engine.
"""

from __future__ import annotations

import time

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
from ml.utils.cross_validation import (
    evaluate_model,
)
from ml.utils.experiment_utils import (
    generate_experiment_id,
)
from ml.utils.training_utils import (
    create_model,
    train_model,
)


class AutoMLEngine:
    """
    Train and rank multiple machine learning models.
    """

    def analyze(
        self,
        dataset: MLDataset,
        configuration: TrainingConfiguration,
    ) -> AutoMLResult:
        """
        Execute the AutoML pipeline.
        """
        trained_models: list[TrainedModel] = []

        start_time = time.perf_counter()

        for model_name in configuration.model_names:
            model = create_model(
                model_name,
            )

            model_start = time.perf_counter()

            trained = train_model(
                model=model,
                features=dataset.features,
                targets=dataset.targets,
            )

            training_time = time.perf_counter() - model_start

            score = evaluate_model(
                model=trained,
                features=dataset.features,
                targets=dataset.targets,
                folds=configuration.cross_validation_folds,
            )

            trained_models.append(
                TrainedModel(
                    model_name=model_name,
                    estimator=trained,
                    score=score,
                    training_time=training_time,
                    feature_count=dataset.feature_count,
                    sample_count=dataset.sample_count,
                )
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
