"""
RNAOS deep learning inference engine.
"""

from __future__ import annotations

from typing import Any

from dl.encoders.inference_encoder import (
    InferenceSequenceEncoder,
)
from dl.models.prediction_request import (
    PredictionRequest,
)
from dl.models.prediction_result import (
    PredictionResult,
)


class DeepLearningInferenceEngine:
    """
    Executes deep learning inference workflows.
    """

    def __init__(
        self,
    ) -> None:
        self.encoder = InferenceSequenceEncoder()

    def predict(
        self,
        model: Any,
        request: PredictionRequest,
    ) -> PredictionResult:
        """
        Execute model prediction.
        """

        encoded_sequence = self.encoder.encode(
            request.sequence,
        )

        prediction = model.predict(
            encoded_sequence,
        )

        value = float(
            prediction[0],
        )

        return PredictionResult(
            prediction_task=(request.prediction_task),
            value=value,
            model_version=(request.model_version),
            confidence=1.0,
            metadata=request.metadata,
        )
