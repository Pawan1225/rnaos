"""
RNAOS explainability pipeline.
"""

from __future__ import annotations

from typing import Any

from dl.explainability.attention_visualization_engine import (
    AttentionVisualizationEngine,
)
from dl.explainability.explanation_report_generator import (
    ExplanationReportGenerator,
)
from dl.explainability.integrated_gradient_analyzer import (
    IntegratedGradientAnalyzer,
)
from dl.explainability.saliency_analyzer import (
    SaliencyAnalyzer,
)
from dl.models.explanation_report import (
    ExplanationReport,
)


class ExplainabilityPipeline:
    """
    Orchestrates explainability workflow.
    """

    def __init__(
        self,
    ) -> None:
        self.saliency = SaliencyAnalyzer()

        self.integrated_gradients = IntegratedGradientAnalyzer()

        self.attention = AttentionVisualizationEngine()

        self.report_generator = ExplanationReportGenerator()

    def run(
        self,
        model: Any,
        prediction_task: str,
        prediction_value: float,
        inputs: tuple[float, ...],
        use_attention: bool = False,
    ) -> ExplanationReport:
        """
        Execute explanation workflow.
        """

        explanations = [
            self.saliency.analyze(
                model=model,
                inputs=inputs,
            ),
            self.integrated_gradients.analyze(
                model=model,
                inputs=inputs,
            ),
        ]

        if use_attention:
            explanations.append(
                self.attention.analyze(
                    model=model,
                    sequence_length=len(inputs),
                )
            )

        return self.report_generator.generate(
            prediction_task=prediction_task,
            prediction_value=prediction_value,
            explanations=tuple(
                explanations,
            ),
        )
