"""
Tests for explanation report generator.
"""

from __future__ import annotations

from dl.explainability.explanation_report_generator import (
    ExplanationReportGenerator,
)
from dl.models.attribution_result import (
    AttributionResult,
)
from dl.models.explanation_report import (
    ExplanationReport,
)


def test_report_generation() -> None:
    """
    Report combines explanations.
    """

    generator = ExplanationReportGenerator()

    explanation = AttributionResult(
        method="saliency",
        features=(
            "A",
            "U",
        ),
        importance_scores=(
            0.2,
            0.8,
        ),
        confidence=0.8,
    )

    report = generator.generate(
        prediction_task="stability",
        prediction_value=0.9,
        explanations=(explanation,),
    )

    assert isinstance(
        report,
        ExplanationReport,
    )

    assert report.prediction_value == 0.9

    assert report.confidence == 0.8

    assert report.completed is True
