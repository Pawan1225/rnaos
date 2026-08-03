"""
RNA Folding Constraint Generator.
"""

from __future__ import annotations

from folding.profilers.folding_profiler import FoldingProfile

from optimization.models.optimization_problem import (
    Constraint,
)


class ConstraintGenerator:
    """
    Generate biologically meaningful optimization constraints.
    """

    def generate(
        self,
        folding_profile: FoldingProfile,
    ) -> list[Constraint]:
        """
        Generate constraints directly from the RNA folding
        conflict graph.
        """

        constraints: list[Constraint] = []

        candidates = folding_profile.search_space.candidates

        for edge in folding_profile.search_space.conflicts:
            first = candidates[edge.first]
            second = candidates[edge.second]

            constraints.append(
                Constraint(
                    name=f"conflict_{edge.first}_{edge.second}",
                    expression=(
                        f"x_{first.left}_{first.right} + x_{second.left}_{second.right} <= 1"
                    ),
                )
            )

        return constraints
