from analytics.models.experiment_record import (
    ExperimentRecord,
)
from analytics.trends import (
    TrendDetector,
    TrendDirection,
)


def test_runtime_improving() -> None:
    records = [
        ExperimentRecord(
            experiment_id="1",
            sequence="A",
            solver="SA",
            objective_value=-10.0,
            runtime_seconds=0.40,
            confidence=0.80,
        ),
        ExperimentRecord(
            experiment_id="2",
            sequence="A",
            solver="SA",
            objective_value=-10.0,
            runtime_seconds=0.30,
            confidence=0.85,
        ),
        ExperimentRecord(
            experiment_id="3",
            sequence="A",
            solver="SA",
            objective_value=-10.0,
            runtime_seconds=0.20,
            confidence=0.90,
        ),
        ExperimentRecord(
            experiment_id="4",
            sequence="A",
            solver="SA",
            objective_value=-10.0,
            runtime_seconds=0.10,
            confidence=0.95,
        ),
    ]

    trend = TrendDetector().detect_runtime(records)

    assert trend is not None
    assert trend.direction == TrendDirection.IMPROVING
    assert trend.current < trend.previous


def test_confidence_improving() -> None:
    records = [
        ExperimentRecord(
            experiment_id="1",
            sequence="A",
            solver="GA",
            objective_value=-10.0,
            runtime_seconds=0.20,
            confidence=0.70,
        ),
        ExperimentRecord(
            experiment_id="2",
            sequence="A",
            solver="GA",
            objective_value=-10.0,
            runtime_seconds=0.20,
            confidence=0.75,
        ),
        ExperimentRecord(
            experiment_id="3",
            sequence="A",
            solver="GA",
            objective_value=-10.0,
            runtime_seconds=0.20,
            confidence=0.90,
        ),
        ExperimentRecord(
            experiment_id="4",
            sequence="A",
            solver="GA",
            objective_value=-10.0,
            runtime_seconds=0.20,
            confidence=0.95,
        ),
    ]

    trend = TrendDetector().detect_confidence(records)

    assert trend is not None
    assert trend.direction == TrendDirection.IMPROVING
    assert trend.current > trend.previous


def test_insufficient_history() -> None:
    trend = TrendDetector().detect_runtime([])

    assert trend is None


def test_stable_runtime() -> None:
    records = [
        ExperimentRecord(
            experiment_id="1",
            sequence="A",
            solver="SA",
            objective_value=-5.0,
            runtime_seconds=0.20,
            confidence=0.90,
        ),
        ExperimentRecord(
            experiment_id="2",
            sequence="A",
            solver="SA",
            objective_value=-5.0,
            runtime_seconds=0.20,
            confidence=0.90,
        ),
    ]

    trend = TrendDetector().detect_runtime(records)

    assert trend is not None
    assert trend.direction == TrendDirection.STABLE
