"""
RNAOS batch inference engine.
"""

from __future__ import annotations

from typing import Any

from dl.engines.inference_engine import (
    DeepLearningInferenceEngine,
)
from dl.models.prediction_request import (
    PredictionRequest,
)
from dl.models.prediction_result import (
    PredictionResult,
)


class BatchInferenceEngine:
    """
    Executes batch deep learning inference.
    """

    def __init__(
        self,
    ) -> None:
        self.inference_engine = DeepLearningInferenceEngine()

    def predict_batch(
        self,
        model: Any,
        requests: tuple[PredictionRequest, ...],
    ) -> tuple[PredictionResult, ...]:
        """
        Execute inference over multiple requests.
        """

        results: list[PredictionResult] = []

        for request in requests:
            result = self.inference_engine.predict(
                model=model,
                request=request,
            )

            results.append(
                result,
            )

        return tuple(
            results,
        )
