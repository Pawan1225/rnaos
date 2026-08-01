"""
Objective Function Generator

Converts an AIProfile into a solver-independent optimization objective.
"""

from __future__ import annotations

from ai_intelligence.profilers.ai_profiler import AIProfile

from optimization.models.optimization_problem import ObjectiveFunction


class ObjectiveFunctionGenerator:
    """Generates optimization objectives."""

    def generate(self, profile: AIProfile) -> ObjectiveFunction:
        """
        Generate an optimization objective.

        Current strategy:
            Minimize predicted optimization complexity.

        Future versions:
            - Minimum Free Energy
            - Stability maximization
            - Multi-objective optimization
            - Learned objectives
        """

        score = profile.complexity.score

        expression = f"minimize_complexity(score={score:.4f})"

        return ObjectiveFunction(
            expression=expression,
            sense="minimize",
        )
