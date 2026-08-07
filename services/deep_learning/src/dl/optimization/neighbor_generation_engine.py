"""
RNAOS neighbor generation engine.
"""

from __future__ import annotations

from dl.models.optimization.local_search_state import (
    LocalSearchState,
)
from dl.models.optimization.neighbor_result import (
    NeighborResult,
)


class NeighborGenerationEngine:
    """
    Generates local search neighbors.
    """

    def generate(
        self,
        state: LocalSearchState,
    ) -> NeighborResult:
        """
        Generate single-bit flip neighbors.
        """

        neighbors: list[LocalSearchState] = []

        for index, value in enumerate(
            state.solution,
        ):
            solution = list(
                state.solution,
            )

            solution[index] = -value

            neighbors.append(
                LocalSearchState(
                    state_id=index,
                    solution=tuple(solution),
                    energy=state.energy,
                    iteration=state.iteration + 1,
                )
            )

        return NeighborResult(
            source_id=state.state_id,
            neighbors=tuple(neighbors),
        )
