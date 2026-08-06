"""
RNAOS deep learning intelligence engine.
"""

from __future__ import annotations

from typing import Any

from dl.engines.model_selection_engine import (
    ModelSelectionEngine,
)
from dl.models.intelligence_request import (
    IntelligenceRequest,
)
from dl.models.intelligence_result import (
    IntelligenceResult,
)
from dl.models.prediction_request import (
    PredictionRequest,
)
from dl.pipelines.explainability_pipeline import (
    ExplainabilityPipeline,
)
from dl.pipelines.inference_pipeline import (
    InferencePipeline,
)


class DeepLearningIntelligenceEngine:
    """
    Executes high-level deep learning intelligence.
    """

    def __init__(
        self,
    ) -> None:
        self.model_selector = ModelSelectionEngine()

        self.inference_pipeline = InferencePipeline()

        self.explainability_pipeline = ExplainabilityPipeline()

    def analyze(
        self,
        model: Any,
        request: IntelligenceRequest,
    ) -> IntelligenceResult:
        """
        Execute intelligence workflow.
        """

        selection = self.model_selector.select(
            request.task,
        )

        prediction_request = PredictionRequest(
            sequence=request.sequence,
            prediction_task=request.task,
            model_version="v1",
            metadata=request.metadata,
        )

        inference_report = self.inference_pipeline.run(
            model=model,
            request=prediction_request,
        )

        explanation = None

        if request.configuration.explanation_enabled:
            encoded_input = tuple(
                float(index)
                for index, _ in enumerate(
                    request.sequence,
                )
            )

            explanation = self.explainability_pipeline.run(
                model=model,
                prediction_task=request.task,
                prediction_value=(inference_report.prediction.value),
                inputs=encoded_input,
            )

        return IntelligenceResult(
            prediction=(inference_report.prediction),
            explanation=explanation,
            selected_model=(selection.model_family),
            confidence=(inference_report.confidence),
            completed=True,
        )
