"""
RNAOS deep learning intelligence pipeline.
"""

from __future__ import annotations

from typing import Any

from dl.engines.deep_learning_intelligence_engine import (
    DeepLearningIntelligenceEngine,
)
from dl.engines.intelligence_evaluation_engine import (
    IntelligenceEvaluationEngine,
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


class DeepLearningIntelligencePipeline:
    """
    Orchestrates complete intelligence workflow.
    """

    def __init__(
        self,
    ) -> None:
        self.intelligence_engine = DeepLearningIntelligenceEngine()

        self.evaluation_engine = IntelligenceEvaluationEngine()

    def run(
        self,
        model: Any,
        request: IntelligenceRequest,
        actual_value: float | None = None,
    ) -> tuple[
        IntelligenceResult,
        IntelligenceEvaluation | None,
    ]:
        """
        Execute intelligence workflow.
        """

        result = self.intelligence_engine.analyze(
            model=model,
            request=request,
        )

        evaluation = None

        if actual_value is not None:
            evaluation = self.evaluation_engine.evaluate(
                predicted=(result.prediction.value),
                actual=actual_value,
            )

        return (
            result,
            evaluation,
        )
