"""
Tests for batch inference engine.
"""

from __future__ import annotations

from dl.engines.batch_inference_engine import (
    BatchInferenceEngine,
)
from dl.models.prediction_request import (
    PredictionRequest,
)


class DummyModel:
    """
    Minimal inference model.
    """

    def predict(
        self,
        inputs,
    ) -> tuple[float, ...]:
        return (0.5,)


def test_batch_prediction_execution() -> None:
    """
    Batch inference returns all results.
    """

    engine = BatchInferenceEngine()

    requests = (
        PredictionRequest(
            sequence="AUGC",
            prediction_task="stability",
        ),
        PredictionRequest(
            sequence="GGCA",
            prediction_task="energy",
        ),
    )

    results = engine.predict_batch(
        model=DummyModel(),
        requests=requests,
    )

    assert len(results) == 2

    assert results[0].value == 0.5

    assert results[1].prediction_task == "energy"
