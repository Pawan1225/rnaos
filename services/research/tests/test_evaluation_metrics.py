from research.metrics.evaluation_metrics import (
    MetricsFactory,
)


def test_metrics_with_reference():
    metrics = MetricsFactory.build(
        benchmark_id="toy_001",
        solver_name="SA",
        objective_value=-6.9,
        runtime_seconds=0.12,
        reference_objective=-7.2,
    )

    assert metrics.absolute_error > 0
    assert metrics.relative_error >= 0
    assert 0.0 <= metrics.accuracy <= 1.0


def test_metrics_without_reference():
    metrics = MetricsFactory.build(
        benchmark_id="toy_001",
        solver_name="GA",
        objective_value=-18.0,
        runtime_seconds=0.4,
    )

    assert metrics.reference_objective is None
    assert metrics.absolute_error == 0.0
    assert metrics.relative_error == 0.0
    assert metrics.accuracy == 1.0


def test_metadata():
    metrics = MetricsFactory.build(
        benchmark_id="toy_001",
        solver_name="Exact",
        objective_value=-10.0,
        runtime_seconds=0.01,
        metadata={
            "sequence_length": 25,
            "candidate_pairs": 50,
            "conflicts": 75,
            "vienna_energy": -20.0,
        },
    )

    assert metrics.metadata["sequence_length"] == 25
    assert metrics.metadata["candidate_pairs"] == 50
