from analytics.history.experiment_history import (
    ExperimentHistory,
)
from analytics.models.experiment_record import (
    ExperimentRecord,
)


def test_add_record() -> None:
    history = ExperimentHistory()

    history.add(
        ExperimentRecord(
            experiment_id="exp1",
            sequence="GGGAAAUCC",
            solver="Exact Solver",
            objective_value=-12.5,
            runtime_seconds=0.15,
            confidence=0.96,
        )
    )

    assert history.count() == 1


def test_latest() -> None:
    history = ExperimentHistory()

    history.add(
        ExperimentRecord(
            experiment_id="1",
            sequence="AAAA",
            solver="SA",
            objective_value=-1.0,
            runtime_seconds=0.1,
            confidence=0.8,
        )
    )

    history.add(
        ExperimentRecord(
            experiment_id="2",
            sequence="CCCC",
            solver="GA",
            objective_value=-2.0,
            runtime_seconds=0.2,
            confidence=0.9,
        )
    )

    latest = history.latest()

    assert latest is not None
    assert latest.experiment_id == "2"


def test_filter_solver() -> None:
    history = ExperimentHistory()

    history.add(
        ExperimentRecord(
            experiment_id="1",
            sequence="AAAA",
            solver="SA",
            objective_value=-1.0,
            runtime_seconds=0.1,
            confidence=0.8,
        )
    )

    history.add(
        ExperimentRecord(
            experiment_id="2",
            sequence="CCCC",
            solver="GA",
            objective_value=-2.0,
            runtime_seconds=0.2,
            confidence=0.9,
        )
    )

    history.add(
        ExperimentRecord(
            experiment_id="3",
            sequence="GGGG",
            solver="SA",
            objective_value=-3.0,
            runtime_seconds=0.3,
            confidence=0.95,
        )
    )

    records = history.by_solver("SA")

    assert len(records) == 2
    assert all(record.solver == "SA" for record in records)
