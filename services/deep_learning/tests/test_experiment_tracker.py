"""
Tests for experiment tracker.
"""

from __future__ import annotations

from dl.models.experiment_record import (
    ExperimentRecord,
)
from dl.registry.experiment_tracker import (
    ExperimentTracker,
)


def test_create_experiment() -> None:
    """
    Experiment can be stored.
    """

    tracker = ExperimentTracker()

    record = ExperimentRecord(
        experiment_id="exp_001",
        model_name="rna_transformer",
        dataset_name="rfam",
        metrics=(
            "accuracy",
            "loss",
        ),
        status="completed",
    )

    tracker.create(
        record,
    )

    result = tracker.get(
        "exp_001",
    )

    assert result == record


def test_list_experiments() -> None:
    """
    Tracker lists experiments.
    """

    tracker = ExperimentTracker()

    tracker.create(
        ExperimentRecord(
            experiment_id="exp_002",
            model_name="rna_cnn",
            dataset_name="pdb",
            metrics=("loss",),
            status="running",
        ),
    )

    assert tracker.list_experiments() == ("exp_002",)
