from analytics.models.experiment_record import (
    ExperimentRecord,
)
from analytics.performance import (
    PerformanceAnalyzer,
)


def test_performance_summary() -> None:
    records = [
        ExperimentRecord(
            experiment_id="1",
            sequence="AAAA",
            solver="SA",
            objective_value=-10,
            runtime_seconds=0.20,
            confidence=0.80,
        ),
        ExperimentRecord(
            experiment_id="2",
            sequence="CCCC",
            solver="SA",
            objective_value=-12,
            runtime_seconds=0.30,
            confidence=0.90,
        ),
        ExperimentRecord(
            experiment_id="3",
            sequence="GGGG",
            solver="GA",
            objective_value=-11,
            runtime_seconds=0.40,
            confidence=0.95,
        ),
    ]

    summary = PerformanceAnalyzer().summarize(records)

    assert len(summary) == 2
    assert summary[0].experiments > 0
    assert summary[1].mean_runtime > 0


def test_single_solver() -> None:
    records = [
        ExperimentRecord(
            experiment_id="1",
            sequence="AAAA",
            solver="Exact",
            objective_value=-5,
            runtime_seconds=0.10,
            confidence=1.0,
        )
    ]

    summary = PerformanceAnalyzer().summarize(records)

    assert len(summary) == 1
    assert summary[0].solver == "Exact"
    assert summary[0].mean_confidence == 1.0


def test_empty_history() -> None:
    summary = PerformanceAnalyzer().summarize([])

    assert summary == []
