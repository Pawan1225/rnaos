"""
RNAOS explanation report generator.
"""

from __future__ import annotations

from dl.models.attribution_result import (
    AttributionResult,
)
from dl.models.explanation_report import (
    ExplanationReport,
)


class ExplanationReportGenerator:
    """
    Generates combined explanation reports.
    """

    def generate(
        self,
        prediction_task: str,
        prediction_value: float,
        explanations: tuple[AttributionResult, ...],
    ) -> ExplanationReport:
        """
        Generate explanation report.
        """

        confidence = max(
            (explanation.confidence for explanation in explanations),
            default=0.0,
        )

        return ExplanationReport(
            prediction_task=prediction_task,
            prediction_value=prediction_value,
            explanations=explanations,
            confidence=confidence,
            completed=True,
        )
