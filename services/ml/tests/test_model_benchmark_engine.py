"""
Tests for the RNAOS Model Benchmark Engine.
"""

from __future__ import annotations

import pytest
from ml.analyzers.model_benchmark_engine import (
    ModelBenchmarkEngine,
)
from ml.models.benchmark_report import (
    BenchmarkReport,
)
from ml.models.trained_model import (
    TrainedModel,
)


def create_model(
    name: str,
    score: float,
) -> TrainedModel:
    """
    Create deterministic trained model.
    """

    return TrainedModel(
        model_name=name,
        estimator=None,
        metric_name="r2",
        metric_value=score,
        training_time=1.0,
        feature_count=10,
        sample_count=100,
        training_status="completed",
    )


@pytest.fixture
def engine() -> ModelBenchmarkEngine:
    """
    Create benchmark engine.
    """

    return ModelBenchmarkEngine()


def test_benchmark_returns_report(
    engine: ModelBenchmarkEngine,
) -> None:
    """
    Benchmark returns BenchmarkReport.
    """

    report = engine.benchmark(
        models=(
            create_model(
                "random_forest",
                0.91,
            ),
        ),
    )

    assert isinstance(
        report,
        BenchmarkReport,
    )


def test_best_model_selection(
    engine: ModelBenchmarkEngine,
) -> None:
    """
    Highest scoring model is selected.
    """

    report = engine.benchmark(
        models=(
            create_model(
                "random_forest",
                0.91,
            ),
            create_model(
                "svm",
                0.85,
            ),
        ),
    )

    assert report.best_model == "random_forest"


def test_scores_preserved(
    engine: ModelBenchmarkEngine,
) -> None:
    """
    Benchmark scores are preserved.
    """

    report = engine.benchmark(
        models=(
            create_model(
                "random_forest",
                0.91,
            ),
        ),
    )

    assert report.model_scores == (
        (
            "random_forest",
            0.91,
        ),
    )


def test_empty_models_fail(
    engine: ModelBenchmarkEngine,
) -> None:
    """
    Empty benchmark input is rejected.
    """

    with pytest.raises(
        ValueError,
    ):
        engine.benchmark(
            models=(),
        )
