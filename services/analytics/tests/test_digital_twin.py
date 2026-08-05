from analytics.digital_twin import (
    DigitalTwinBuilder,
    HealthStatus,
)
from analytics.models.experiment_record import (
    ExperimentRecord,
)
from analytics.performance import (
    PerformanceAnalyzer,
)


def test_digital_twin() -> None:
    records = [
        ExperimentRecord(
            experiment_id="1",
            sequence="AAAA",
            solver="SA",
            objective_value=-10.0,
            runtime_seconds=0.10,
            confidence=0.90,
        ),
        ExperimentRecord(
            experiment_id="2",
            sequence="CCCC",
            solver="GA",
            objective_value=-12.0,
            runtime_seconds=0.20,
            confidence=0.95,
        ),
    ]

    performance = PerformanceAnalyzer().summarize(records)

    twin = DigitalTwinBuilder().build(
        records=records,
        performance=performance,
        benchmark_accuracy=0.93,
    )

    assert twin.total_experiments == 2
    assert twin.health == HealthStatus.HEALTHY
    assert len(twin.active_solvers) == 2
    assert twin.average_runtime > 0.0
    assert twin.average_confidence > 0.0
    assert twin.latest_experiment is not None
    assert twin.latest_experiment.experiment_id == "2"


def test_warning_health() -> None:
    twin = DigitalTwinBuilder().build(
        records=[],
        performance=[],
        benchmark_accuracy=0.70,
    )

    assert twin.health == HealthStatus.WARNING


def test_critical_health() -> None:
    twin = DigitalTwinBuilder().build(
        records=[],
        performance=[],
        benchmark_accuracy=0.50,
    )

    assert twin.health == HealthStatus.CRITICAL


def test_empty_digital_twin() -> None:
    twin = DigitalTwinBuilder().build(
        records=[],
        performance=[],
        benchmark_accuracy=1.0,
    )

    assert twin.total_experiments == 0
    assert twin.active_solvers == []
    assert twin.latest_experiment is None
    assert twin.average_runtime == 0.0
    assert twin.average_confidence == 0.0
    assert twin.health == HealthStatus.HEALTHY
