"""
Tests for integrated gradient analyzer.
"""

from __future__ import annotations

from dl.explainability.integrated_gradient_analyzer import (
    IntegratedGradientAnalyzer,
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


def test_integrated_gradient_generation() -> None:
    """
    Generates attribution result.
    """

    analyzer = IntegratedGradientAnalyzer()

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

    assert result.method == "integrated_gradients"

    assert result.importance_scores == (
        1.0,
        2.0,
        3.0,
    )


def test_custom_baseline() -> None:
    """
    Uses custom baseline values.
    """

    analyzer = IntegratedGradientAnalyzer()

    result = analyzer.analyze(
        model=DummyModel(),
        inputs=(
            2.0,
            4.0,
        ),
        baseline=(
            1.0,
            1.0,
        ),
    )

    assert result.importance_scores == (
        1.0,
        3.0,
    )
