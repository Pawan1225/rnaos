"""
Tests for deep learning intelligence pipeline.
"""

from __future__ import annotations

from dl.models.intelligence_configuration import (
    IntelligenceConfiguration,
)
from dl.models.intelligence_evaluation import (
    IntelligenceEvaluation,
)
from dl.models.intelligence_request import (
    IntelligenceRequest,
)
from dl.models.intelligence_result import (
    IntelligenceResult,
)
from dl.pipelines.intelligence_pipeline import (
    DeepLearningIntelligencePipeline,
)


class DummyModel:
    """
    Minimal deep learning model.
    """

    def predict(
        self,
        inputs,
    ) -> tuple[float, ...]:
        return (0.85,)


def test_intelligence_pipeline_execution() -> None:
    """
    Pipeline completes intelligence workflow.
    """

    pipeline = DeepLearningIntelligencePipeline()

    request = IntelligenceRequest(
        sequence="AUGC",
        task="rna_sequence_analysis",
        configuration=(IntelligenceConfiguration()),
    )

    result, evaluation = pipeline.run(
        model=DummyModel(),
        request=request,
    )

    assert isinstance(
        result,
        IntelligenceResult,
    )

    assert result.completed is True

    assert result.selected_model == "transformer"

    assert result.prediction.value == 0.85

    assert evaluation is None


def test_intelligence_pipeline_with_evaluation() -> None:
    """
    Pipeline returns evaluation when ground truth exists.
    """

    pipeline = DeepLearningIntelligencePipeline()

    request = IntelligenceRequest(
        sequence="AUGC",
        task="rna_sequence_analysis",
        configuration=(IntelligenceConfiguration()),
    )

    result, evaluation = pipeline.run(
        model=DummyModel(),
        request=request,
        actual_value=0.80,
    )

    assert isinstance(
        result,
        IntelligenceResult,
    )

    assert isinstance(
        evaluation,
        IntelligenceEvaluation,
    )

    assert evaluation.absolute_error == 0.05

    assert evaluation.passed_threshold is True
