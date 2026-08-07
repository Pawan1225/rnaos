"""
RNAOS objective function engine.
"""

from __future__ import annotations

from dl.models.optimization.objective_function import (
    ObjectiveFunction,
)


class ObjectiveFunctionEngine:
    """
    Builds RNA optimization objectives.
    """

    def create(
        self,
        terms: tuple[float, ...],
    ) -> ObjectiveFunction:
        """
        Create energy minimization objective.
        """

        if not terms:
            raise ValueError(
                "Objective requires terms",
            )

        return ObjectiveFunction(
            name="rna_energy_minimization",
            terms=terms,
            minimize=True,
        )
