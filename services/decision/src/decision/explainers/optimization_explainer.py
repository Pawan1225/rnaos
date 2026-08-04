"""
Optimization Explanation Engine.
"""

from __future__ import annotations

from optimization.models.optimization_problem import (
    QUBOProblem,
)

from decision.models import (
    DecisionReason,
    Evidence,
    Explanation,
)


class OptimizationExplainer:
    """
    Explain how an optimization problem was formulated.

    This explainer converts a Scientific QUBO into a structured,
    evidence-backed explanation describing the optimization model,
    objective, constraints, and thermodynamic formulation.
    """

    def explain(
        self,
        problem: QUBOProblem,
    ) -> Explanation:
        """Generate an explanation for a QUBO formulation."""

        reasons: list[DecisionReason] = []

        variable_count = problem.size
        penalty = problem.penalty

        #
        # Decision variables
        #

        reasons.append(
            DecisionReason(
                title="Decision Variables",
                description=(
                    f"The optimization problem contains "
                    f"{variable_count} binary decision variables "
                    "representing candidate RNA base pairs."
                ),
                importance=0.95,
                evidence=[
                    Evidence(
                        name="Variable Count",
                        value=variable_count,
                        description=("Number of binary optimization variables."),
                        source="QUBOGenerator",
                        weight=0.95,
                    ),
                ],
            )
        )

        #
        # Objective
        #

        reasons.append(
            DecisionReason(
                title="Objective Function",
                description=(
                    "The optimization objective minimizes RNA folding "
                    "energy while maximizing structural stability."
                ),
                importance=0.90,
            )
        )

        #
        # Thermodynamics
        #

        reasons.append(
            DecisionReason(
                title="Thermodynamic Model",
                description=(
                    "Nearest-neighbor interactions, stacking energies, "
                    "and loop energetics contribute to the optimization "
                    "objective."
                ),
                importance=0.85,
            )
        )

        #
        # Constraints
        #

        reasons.append(
            DecisionReason(
                title="Constraints",
                description=(
                    "Penalty terms prevent incompatible base-pair "
                    "assignments and enforce valid RNA structures."
                ),
                importance=0.90,
                evidence=[
                    Evidence(
                        name="Penalty Weight",
                        value=penalty,
                        description=("Constraint penalty coefficient."),
                        source="QUBOGenerator",
                        weight=0.90,
                    ),
                ],
            )
        )

        return Explanation(
            recommendation="Scientific QUBO Formulation",
            confidence=1.0,
            reasons=reasons,
            alternatives=[],
            tradeoffs=[
                "Provides a mathematically rigorous optimization model.",
                "Can be solved by classical, quantum, and hybrid solvers.",
            ],
            metadata={
                "variables": variable_count,
                "penalty": penalty,
            },
        )
