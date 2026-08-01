"""
Constraint Generator

Generates solver-independent optimization constraints.
"""

from __future__ import annotations

from ai_intelligence.profilers.ai_profiler import AIProfile

from optimization.models.optimization_problem import Constraint


class ConstraintGenerator:
    """Generates optimization constraints."""

    def generate(self, profile: AIProfile) -> list[Constraint]:
        """
        Generate optimization constraints.

        Current constraints:
            - Binary decision variables
            - Variable bounds

        Future constraints:
            - RNA base-pair compatibility
            - Hairpin loop rules
            - Stem continuity
            - Pseudoknot restrictions
            - Energy constraints
        """

        sequence_length = profile.features.values[0]

        constraints = [
            Constraint(
                name="binary_variables",
                expression="x_i ∈ {0,1}",
            ),
            Constraint(
                name="sequence_length",
                expression=f"number_of_variables = {int(sequence_length)}",
            ),
        ]

        return constraints
