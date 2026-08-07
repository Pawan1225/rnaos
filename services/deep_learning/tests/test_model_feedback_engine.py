"""
Tests for model feedback engine.
"""

from __future__ import annotations

from dl.continuous_learning.feedback.model_feedback_engine import (
    ModelFeedbackEngine,
)


def test_healthy_model_feedback() -> None:
    """
    Healthy model is detected.
    """

    engine = ModelFeedbackEngine()

    feedback = engine.evaluate(
        model_id="DL_MODEL_001",
        prediction=0.90,
        actual=0.92,
        confidence=0.95,
    )

    assert feedback.drift_detected is False

    assert feedback.retraining_required is False

    assert feedback.recommendation == ("model_healthy")


def test_drift_detection() -> None:
    """
    Model drift is detected.
    """

    engine = ModelFeedbackEngine()

    feedback = engine.evaluate(
        model_id="DL_MODEL_001",
        prediction=0.50,
        actual=0.90,
        confidence=0.40,
    )

    assert feedback.drift_detected is True

    assert feedback.retraining_required is True

    assert feedback.recommendation == ("retrain_model")
