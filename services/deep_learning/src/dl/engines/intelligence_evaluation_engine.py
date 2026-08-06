"""
RNAOS intelligence evaluation engine.
"""

from __future__ import annotations

from dl.models.intelligence_evaluation import (
    IntelligenceEvaluation,
)


class IntelligenceEvaluationEngine:
    """
    Evaluates intelligence predictions.
    """

    def evaluate(
        self,
        predicted: float,
        actual: float,
        threshold: float = 0.1,
    ) -> IntelligenceEvaluation:
        """
        Compare prediction with actual value.
        """

        error = round(
            predicted - actual,
            10,
        )

        absolute_error = round(
            abs(error),
            10,
        )

        return IntelligenceEvaluation(
            error=error,
            absolute_error=absolute_error,
            passed_threshold=(absolute_error <= threshold),
        )
