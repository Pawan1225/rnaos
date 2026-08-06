"""
RNAOS machine learning model evaluation engine.
"""

from __future__ import annotations

from math import isfinite

from ml.models.ml_dataset import (
    MLDataset,
)
from ml.models.model_evaluation import (
    ModelEvaluation,
)
from ml.models.trained_model import (
    TrainedModel,
)
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


class ModelEvaluationEngine:
    """
    Evaluates trained machine learning models.

    Responsible only for calculating regression
    metrics and returning ModelEvaluation.
    """

    def evaluate(
        self,
        trained_model: TrainedModel,
        dataset: MLDataset,
    ) -> ModelEvaluation:
        """
        Evaluate a trained model on the test dataset.
        """

        self._validate_inputs(
            trained_model,
            dataset,
        )

        features, targets = self._extract_test_data(
            dataset,
        )

        predictions = trained_model.estimator.predict(
            features,
        )

        metrics = self._calculate_metrics(
            targets,
            predictions,
        )

        return ModelEvaluation(
            model_name=trained_model.model_name,
            metrics=metrics,
            evaluation_version="v1",
            sample_count=len(targets),
        )

    def _extract_test_data(
        self,
        dataset: MLDataset,
    ) -> tuple[list[list[float]], list[float]]:
        """
        Extract test partition from dataset.
        """

        features = [list(dataset.features[index]) for index in dataset.test_indices]

        targets = [dataset.targets[index] for index in dataset.test_indices]

        return features, targets

    def _calculate_metrics(
        self,
        targets: list[float],
        predictions,
    ) -> dict[str, float]:
        """
        Calculate regression metrics.
        """

        metrics = {
            "rmse": float(
                mean_squared_error(
                    targets,
                    predictions,
                    squared=False,
                )
            ),
            "mae": float(
                mean_absolute_error(
                    targets,
                    predictions,
                )
            ),
            "r2": float(
                r2_score(
                    targets,
                    predictions,
                )
            ),
        }

        self._validate_metrics(
            metrics,
        )

        return metrics

    def _validate_inputs(
        self,
        trained_model: TrainedModel,
        dataset: MLDataset,
    ) -> None:
        """
        Validate evaluation inputs.
        """

        if not trained_model.is_trained:
            raise ValueError(
                "Model is not trained.",
            )

        if dataset.test_size == 0:
            raise ValueError(
                "Dataset test partition is empty.",
            )

    def _validate_metrics(
        self,
        metrics: dict[str, float],
    ) -> None:
        """
        Ensure generated metrics are finite.
        """

        if not all(isfinite(value) for value in metrics.values()):
            raise ValueError(
                "Evaluation metrics contain non-finite values.",
            )
