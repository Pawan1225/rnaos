"""
RNAOS experiment tracking system.
"""

from __future__ import annotations

from dl.models.experiment_record import (
    ExperimentRecord,
)


class ExperimentTracker:
    """
    Tracks deep learning experiments.
    """

    def __init__(
        self,
    ) -> None:
        self._experiments: dict[
            str,
            ExperimentRecord,
        ] = {}

    def create(
        self,
        record: ExperimentRecord,
    ) -> None:
        """
        Store experiment record.
        """

        self._experiments[record.experiment_id] = record

    def get(
        self,
        experiment_id: str,
    ) -> ExperimentRecord:
        """
        Retrieve experiment.
        """

        return self._experiments[experiment_id]

    def list_experiments(
        self,
    ) -> tuple[str, ...]:
        """
        List experiment IDs.
        """

        return tuple(
            self._experiments.keys(),
        )
