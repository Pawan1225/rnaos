from research.metrics.evaluation_metrics import (
    MetricsFactory,
)
from research.models.experiment_result import (
    ExperimentResult,
)


def test_experiment_result():

    metrics = MetricsFactory.build(
        benchmark_id="toy001",
        solver_name="SA",
        objective_value=-5.0,
        runtime_seconds=0.2,
    )

    result = ExperimentResult(
        benchmark_id="toy001",
        metrics=metrics,
    )

    assert result.successful

    assert result.benchmark_id == "toy001"

    assert result.metrics.solver_name == "SA"


def test_metadata():

    metrics = MetricsFactory.build(
        benchmark_id="toy001",
        solver_name="Exact",
        objective_value=-8,
        runtime_seconds=0.01,
    )

    result = ExperimentResult(
        benchmark_id="toy001",
        metrics=metrics,
        metadata={
            "dataset": "toy",
        },
    )

    assert result.metadata["dataset"] == "toy"
