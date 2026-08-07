"""
RNAOS experiment repository.
"""

from __future__ import annotations

from dl.models.learning.experiment_record import (
    ExperimentRecord,
)


class ExperimentRepository:
    """
    Stores learning experiment records.
    """

    def __init__(self) -> None:
        self._records: list[ExperimentRecord] = []

    def add(
        self,
        record: ExperimentRecord,
    ) -> None:
        """
        Store experiment record.
        """

        self._records.append(
            record,
        )

    def get_all(
        self,
    ) -> tuple[
        ExperimentRecord,
        ...,
    ]:
        """
        Return all experiments.
        """

        return tuple(
            self._records,
        )

    def count(
        self,
    ) -> int:
        """
        Return experiment count.
        """

        return len(
            self._records,
        )

    def get_by_solver(
        self,
        solver: str,
    ) -> tuple[
        ExperimentRecord,
        ...,
    ]:
        """
        Retrieve experiments by solver.
        """

        return tuple(record for record in self._records if record.selected_solver == solver)
