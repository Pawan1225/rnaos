"""
Tests for attention visualization engine.
"""

from __future__ import annotations

from dl.explainability.attention_visualization_engine import (
    AttentionVisualizationEngine,
)
from dl.models.attribution_result import (
    AttributionResult,
)


class DummyTransformer:
    """
    Minimal attention model.
    """

    def get_attention(
        self,
    ) -> tuple[float, ...]:
        return (
            0.1,
            0.3,
            0.9,
            0.2,
        )


def test_attention_generation() -> None:
    """
    Attention produces attribution.
    """

    engine = AttentionVisualizationEngine()

    result = engine.analyze(
        model=DummyTransformer(),
        sequence_length=4,
    )

    assert isinstance(
        result,
        AttributionResult,
    )

    assert result.method == "attention"

    assert result.importance_scores == (
        0.1,
        0.3,
        0.9,
        0.2,
    )


def test_attention_confidence() -> None:
    """
    Confidence uses strongest attention.
    """

    engine = AttentionVisualizationEngine()

    result = engine.analyze(
        model=DummyTransformer(),
        sequence_length=4,
    )

    assert result.confidence == 0.9
