"""
RNA Folding Objective Generator.
"""

from __future__ import annotations

from folding.profilers.folding_profiler import FoldingProfile

from optimization.models.optimization_problem import (
    ObjectiveFunction,
)


class ObjectiveFunctionGenerator:
    """
    Generate biologically meaningful optimization objectives.
    """

    def generate(
        self,
        folding_profile: FoldingProfile,
    ) -> ObjectiveFunction:
        """
        Generate a thermodynamic objective.

        Version 1:
        Minimize the free-energy gap relative to the
        minimum free-energy (MFE) structure.
        """

        thermodynamics = folding_profile.thermodynamics

        expression = f"Minimize ΔG (MFE={thermodynamics.mfe:.2f} kcal/mol)"

        return ObjectiveFunction(
            expression=expression,
        )
