"""
Tests for the RNAOS Model Evaluation Engine.
"""

from __future__ import annotations

from math import isfinite

from ml.models.model_evaluation import (
    ModelEvaluation,
)


def assert_finite_metrics(
    evaluation: ModelEvaluation,
) -> None:
    """
    Validate evaluation metrics.
    """

    for value in evaluation.metrics.values():
        assert isfinite(value)


def test_evaluation_returns_model_evaluation(
    evaluation_engine,
    trained_model,
    dataset,
) -> None:
    """
    Evaluation returns ModelEvaluation.
    """

    result = evaluation_engine.evaluate(
        trained_model,
        dataset,
    )

    assert isinstance(
        result,
        ModelEvaluation,
    )


def test_evaluation_metadata(
    evaluation_engine,
    trained_model,
    dataset,
) -> None:
    """
    Evaluation metadata is preserved.
    """

    result = evaluation_engine.evaluate(
        trained_model,
        dataset,
    )

    assert result.model_name == trained_model.model_name

    assert result.evaluation_version == "v1"

    assert result.sample_count == dataset.test_size


def test_regression_metrics(
    evaluation_engine,
    trained_model,
    dataset,
) -> None:
    """
    Regression metrics are generated.
    """

    result = evaluation_engine.evaluate(
        trained_model,
        dataset,
    )

    assert "rmse" in result.metrics
    assert "mae" in result.metrics
    assert "r2" in result.metrics

    assert_finite_metrics(
        result,
    )


def test_evaluation_is_deterministic(
    evaluation_engine,
    trained_model,
    dataset,
) -> None:
    """
    Same input produces same evaluation.
    """

    first = evaluation_engine.evaluate(
        trained_model,
        dataset,
    )

    second = evaluation_engine.evaluate(
        trained_model,
        dataset,
    )

    assert first.metrics == second.metrics
