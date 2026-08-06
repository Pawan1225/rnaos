"""
Tests for inference pipeline.
"""

from __future__ import annotations

from dl.models.inference_report import (
    InferenceReport,
)
from dl.models.prediction_request import (
    PredictionRequest,
)
from dl.pipelines.inference_pipeline import (
    InferencePipeline,
)


class DummyModel:
    """
    Minimal inference model.
    """

    def predict(
        self,
        inputs,
    ) -> tuple[float, ...]:
        return (0.75,)


def test_inference_pipeline_execution() -> None:
    """
    Pipeline completes inference.
    """

    pipeline = InferencePipeline()

    request = PredictionRequest(
        sequence="AUGC",
        prediction_task="stability",
    )

    report = pipeline.run(
        model=DummyModel(),
        request=request,
    )

    assert isinstance(
        report,
        InferenceReport,
    )

    assert report.completed is True

    assert report.prediction.value == 0.75

    assert report.confidence == 0.75
