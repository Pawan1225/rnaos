"""
RNAOS tabu list manager.
"""

from __future__ import annotations

from dl.models.optimization.tabu_list_result import (
    TabuListResult,
)


class TabuListManager:
    """
    Maintains tabu states.
    """

    def add(
        self,
        states: tuple[tuple[int, ...], ...],
        new_state: tuple[int, ...],
        tenure: int,
    ) -> TabuListResult:
        """
        Add a state while respecting tabu tenure.
        """

        if tenure <= 0:
            raise ValueError(
                "Tenure must be positive",
            )

        updated = states + (new_state,)

        if len(updated) > tenure:
            updated = updated[-tenure:]

        return TabuListResult(
            states=updated,
            size=len(updated),
        )

    def contains(
        self,
        states: tuple[tuple[int, ...], ...],
        state: tuple[int, ...],
    ) -> bool:
        """
        Check whether a state is tabu.
        """

        return state in states
