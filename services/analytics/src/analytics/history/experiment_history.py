"""
Experiment history manager.
"""

from __future__ import annotations

from analytics.models.experiment_record import ExperimentRecord


class ExperimentHistory:
    """Stores experiment history."""

    def __init__(self) -> None:
        self._records: list[ExperimentRecord] = []

    def add(
        self,
        record: ExperimentRecord,
    ) -> None:
        """Add an experiment record."""
        self._records.append(record)

    def all(
        self,
    ) -> list[ExperimentRecord]:
        """Return all experiment records."""
        return list(self._records)

    def count(self) -> int:
        """Return the number of stored experiments."""
        return len(self._records)

    def latest(
        self,
    ) -> ExperimentRecord | None:
        """Return the most recent experiment."""
        if not self._records:
            return None

        return self._records[-1]

    def by_solver(
        self,
        solver: str,
    ) -> list[ExperimentRecord]:
        """Return experiments executed with the given solver."""
        return [record for record in self._records if record.solver == solver]
