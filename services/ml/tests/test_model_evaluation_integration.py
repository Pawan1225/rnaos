"""
Integration tests for the RNAOS Model Evaluation pipeline.
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


def test_training_to_evaluation_pipeline(
    training_engine,
    evaluation_engine,
    dataset,
    configuration,
) -> None:
    """
    Validate complete training and evaluation workflow.
    """

    trained_model = training_engine.analyze(
        dataset=dataset,
        configuration=configuration,
    )

    evaluation = evaluation_engine.evaluate(
        trained_model=trained_model,
        dataset=dataset,
    )

    assert isinstance(
        evaluation,
        ModelEvaluation,
    )

    assert evaluation.model_name == trained_model.model_name

    assert evaluation.evaluation_version == "v1"

    assert evaluation.sample_count == dataset.test_size

    assert_finite_metrics(
        evaluation,
    )


def test_evaluation_reproducibility(
    training_engine,
    evaluation_engine,
    dataset,
    configuration,
) -> None:
    """
    Validate deterministic pipeline behavior.
    """

    first_model = training_engine.analyze(
        dataset=dataset,
        configuration=configuration,
    )

    first_result = evaluation_engine.evaluate(
        trained_model=first_model,
        dataset=dataset,
    )

    second_model = training_engine.analyze(
        dataset=dataset,
        configuration=configuration,
    )

    second_result = evaluation_engine.evaluate(
        trained_model=second_model,
        dataset=dataset,
    )

    assert first_result.metrics == second_result.metrics
