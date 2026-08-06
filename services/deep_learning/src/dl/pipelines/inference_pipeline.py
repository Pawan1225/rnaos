"""
RNAOS deep learning inference pipeline.
"""

from __future__ import annotations

from typing import Any

from dl.engines.confidence_estimator import (
    ConfidenceEstimator,
)
from dl.engines.inference_engine import (
    DeepLearningInferenceEngine,
)
from dl.models.inference_report import (
    InferenceReport,
)
from dl.models.prediction_request import (
    PredictionRequest,
)


class InferencePipeline:
    """
    Orchestrates inference lifecycle.
    """

    def __init__(
        self,
    ) -> None:
        self.inference_engine = DeepLearningInferenceEngine()

        self.confidence_estimator = ConfidenceEstimator()

    def run(
        self,
        model: Any,
        request: PredictionRequest,
    ) -> InferenceReport:
        """
        Execute complete inference workflow.
        """

        prediction = self.inference_engine.predict(
            model=model,
            request=request,
        )

        confidence = self.confidence_estimator.estimate(
            prediction.value,
        )

        return InferenceReport(
            prediction=prediction,
            confidence=confidence,
            completed=True,
        )
