"""
Tests for explainability pipeline.
"""

from __future__ import annotations

from dl.models.explanation_report import (
    ExplanationReport,
)
from dl.pipelines.explainability_pipeline import (
    ExplainabilityPipeline,
)


class DummyModel:
    """
    Minimal explainable model.
    """

    def predict(
        self,
        inputs,
    ) -> tuple[float, ...]:
        return (0.8,)

    def get_attention(
        self,
    ) -> tuple[float, ...]:
        return (
            0.1,
            0.5,
            0.9,
        )


def test_explainability_pipeline() -> None:
    """
    Pipeline generates explanation report.
    """

    pipeline = ExplainabilityPipeline()

    report = pipeline.run(
        model=DummyModel(),
        prediction_task="stability",
        prediction_value=0.8,
        inputs=(
            1.0,
            2.0,
            3.0,
        ),
    )

    assert isinstance(
        report,
        ExplanationReport,
    )

    assert report.completed is True

    assert (
        len(
            report.explanations,
        )
        == 2
    )
