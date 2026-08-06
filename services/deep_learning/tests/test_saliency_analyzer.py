"""
Tests for saliency analyzer.
"""

from __future__ import annotations

from dl.explainability.saliency_analyzer import (
    SaliencyAnalyzer,
)
from dl.models.attribution_result import (
    AttributionResult,
)


class DummyModel:
    """
    Minimal model.
    """

    def predict(
        self,
        inputs,
    ) -> tuple[float, ...]:
        return (0.8,)


def test_saliency_generation() -> None:
    """
    Saliency produces attribution result.
    """

    analyzer = SaliencyAnalyzer()

    result = analyzer.analyze(
        model=DummyModel(),
        inputs=(
            1.0,
            2.0,
            3.0,
        ),
    )

    assert isinstance(
        result,
        AttributionResult,
    )

    assert result.method == "saliency"

    assert result.importance_scores == (
        1.0,
        2.0,
        3.0,
    )


def test_saliency_confidence() -> None:
    """
    Confidence is calculated.
    """

    analyzer = SaliencyAnalyzer()

    result = analyzer.analyze(
        model=DummyModel(),
        inputs=(
            0.1,
            0.9,
        ),
    )

    assert result.confidence == 0.9
