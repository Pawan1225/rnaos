"""
RNAOS prediction engine.
"""

from __future__ import annotations

from datetime import (
    UTC,
    datetime,
)
from math import (
    isfinite,
)

from ai.models.feature_vector import (
    FeatureVector,
)
from ml.models.prediction_result import (
    PredictionResult,
)
from ml.models.trained_model import (
    TrainedModel,
)


class PredictionEngine:
    """
    Generate biological predictions from a trained model.
    """

    def analyze(
        self,
        trained_model: TrainedModel,
        features: FeatureVector,
        experiment_id: str,
    ) -> PredictionResult:
        """
        Generate predictions using a trained model.
        """

        self._validate_features(
            features,
        )

        prediction = self._predict(
            trained_model=trained_model,
            features=features,
        )

        return self._build_result(
            trained_model=trained_model,
            prediction=prediction,
            experiment_id=experiment_id,
        )

    def _predict(
        self,
        trained_model: TrainedModel,
        features: FeatureVector,
    ) -> float:
        """
        Generate a prediction from the trained model.
        """

        return float(
            trained_model.estimator.predict(
                [list(features.values)],
            )[0]
        )

    def _build_result(
        self,
        trained_model: TrainedModel,
        prediction: float,
        experiment_id: str,
    ) -> PredictionResult:
        """
        Build an immutable prediction result.
        """

        confidence = self._confidence_score(
            prediction,
        )

        return PredictionResult(
            folding_difficulty=prediction,
            expected_mfe=prediction,
            structural_stability=prediction,
            solver_suitability=prediction,
            runtime_estimation=prediction,
            optimization_complexity=prediction,
            confidence_score=confidence,
            model_name=trained_model.model_name,
            experiment_id=experiment_id,
            prediction_timestamp=datetime.now(
                UTC,
            ).isoformat(),
        )

    def _confidence_score(
        self,
        prediction: float,
    ) -> float:
        """
        Compute a deterministic confidence score.

        Placeholder implementation that will
        later be replaced with calibrated
        uncertainty estimation.
        """

        return max(
            0.0,
            min(
                1.0,
                1.0
                - abs(
                    prediction,
                )
                / 100.0,
            ),
        )

    def _validate_features(
        self,
        features: FeatureVector,
    ) -> None:
        """
        Validate the prediction features.
        """

        if features.size == 0:
            raise ValueError(
                "Feature vector cannot be empty.",
            )

        if not all(
            isfinite(
                value,
            )
            for value in features.values
        ):
            raise ValueError(
                "Feature vector contains non-finite values.",
            )
