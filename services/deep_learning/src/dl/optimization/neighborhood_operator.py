"""
RNAOS variable neighborhood operator.
"""

from __future__ import annotations

from dl.models.optimization.local_search_state import (
    LocalSearchState,
)
from dl.models.optimization.neighborhood_operator_result import (
    NeighborhoodOperatorResult,
)


class NeighborhoodOperator:
    """
    Generates neighborhood perturbations.
    """

    def generate(
        self,
        state: LocalSearchState,
        level: int,
    ) -> NeighborhoodOperatorResult:
        """
        Generate a deterministic neighbor for the
        requested neighborhood level.
        """

        if level <= 0:
            raise ValueError(
                "Neighborhood level must be positive",
            )

        solution = list(
            state.solution,
        )

        flips = min(
            level,
            len(solution),
        )

        for index in range(flips):
            solution[index] = -solution[index]

        neighbor = LocalSearchState(
            state_id=state.state_id,
            solution=tuple(solution),
            energy=state.energy,
            iteration=state.iteration + 1,
        )

        return NeighborhoodOperatorResult(
            level=level,
            state=neighbor,
        )
