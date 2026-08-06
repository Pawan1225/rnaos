"""
Tests for deep learning intelligence engine.
"""

from __future__ import annotations

from dl.engines.deep_learning_intelligence_engine import (
    DeepLearningIntelligenceEngine,
)
from dl.models.intelligence_configuration import (
    IntelligenceConfiguration,
)
from dl.models.intelligence_request import (
    IntelligenceRequest,
)
from dl.models.intelligence_result import (
    IntelligenceResult,
)


class DummyModel:
    """
    Minimal intelligence model.
    """

    def predict(
        self,
        inputs,
    ) -> tuple[float, ...]:
        return (0.85,)


def test_intelligence_execution() -> None:
    """
    Intelligence workflow completes.
    """

    engine = DeepLearningIntelligenceEngine()

    request = IntelligenceRequest(
        sequence="AUGC",
        task="rna_sequence_analysis",
        configuration=(IntelligenceConfiguration()),
    )

    result = engine.analyze(
        model=DummyModel(),
        request=request,
    )

    assert isinstance(
        result,
        IntelligenceResult,
    )

    assert result.completed is True

    assert result.selected_model == "transformer"

    assert result.confidence == 0.85
