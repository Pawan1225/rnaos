"""
Tests for deep learning inference engine.
"""

from __future__ import annotations

from dl.engines.inference_engine import (
    DeepLearningInferenceEngine,
)
from dl.models.prediction_request import (
    PredictionRequest,
)
from dl.models.prediction_result import (
    PredictionResult,
)


class DummyModel:
    """
    Minimal inference model.
    """

    def predict(
        self,
        inputs,
    ) -> tuple[float, ...]:
        return (0.85,)


def test_inference_execution() -> None:
    """
    Inference produces prediction result.
    """

    engine = DeepLearningInferenceEngine()

    request = PredictionRequest(
        sequence="AUGC",
        prediction_task="stability",
    )

    result = engine.predict(
        model=DummyModel(),
        request=request,
    )

    assert isinstance(
        result,
        PredictionResult,
    )

    assert result.value == 0.85

    assert result.prediction_task == "stability"


def test_inference_metadata() -> None:
    """
    Metadata is preserved.
    """

    engine = DeepLearningInferenceEngine()

    request = PredictionRequest(
        sequence="AUGC",
        prediction_task="energy",
        metadata=("experiment_001",),
    )

    result = engine.predict(
        model=DummyModel(),
        request=request,
    )

    assert result.metadata == ("experiment_001",)
