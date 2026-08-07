"""
RNAOS model feedback engine.
"""

from __future__ import annotations

from dl.models.learning.model_feedback import (
    ModelFeedback,
)


class ModelFeedbackEngine:
    """
    Evaluates model performance feedback.
    """

    def evaluate(
        self,
        model_id: str,
        prediction: float,
        actual: float,
        confidence: float,
    ) -> ModelFeedback:
        """
        Generate model feedback.
        """

        error = abs(
            prediction - actual,
        )

        drift_detected = error > 0.20

        retraining_required = error > 0.30

        if retraining_required:
            recommendation = "retrain_model"
        elif drift_detected:
            recommendation = "monitor_drift"
        else:
            recommendation = "model_healthy"

        return ModelFeedback(
            model_id=model_id,
            prediction_error=error,
            confidence_score=confidence,
            drift_detected=drift_detected,
            retraining_required=retraining_required,
            recommendation=recommendation,
        )
