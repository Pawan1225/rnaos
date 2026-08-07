"""
RNAOS adaptive solver selector.
"""

from __future__ import annotations

from dl.models.optimization.adaptive_solver_selection import (
    AdaptiveSolverSelection,
)


class AdaptiveSolverSelector:
    """
    Dynamically selects solver strategies.
    """

    def select(
        self,
        sequence_length: int,
        complexity: float,
        constraint_density: float,
    ) -> AdaptiveSolverSelection:
        """
        Select adaptive solver strategy.
        """

        if complexity > 0.8:
            return AdaptiveSolverSelection(
                primary_solver="annealing",
                solver_weights=(
                    (
                        "annealing",
                        0.6,
                    ),
                    (
                        "tensor",
                        0.3,
                    ),
                    (
                        "qubo",
                        0.1,
                    ),
                ),
                reasoning=("High complexity requires exploration."),
            )

        if sequence_length > 500:
            return AdaptiveSolverSelection(
                primary_solver="tensor",
                solver_weights=(
                    (
                        "tensor",
                        0.6,
                    ),
                    (
                        "annealing",
                        0.3,
                    ),
                    (
                        "qubo",
                        0.1,
                    ),
                ),
                reasoning=("Large problems benefit from compression."),
            )

        if constraint_density > 0.5:
            return AdaptiveSolverSelection(
                primary_solver="qubo",
                solver_weights=(
                    (
                        "qubo",
                        0.7,
                    ),
                    (
                        "annealing",
                        0.2,
                    ),
                    (
                        "tensor",
                        0.1,
                    ),
                ),
                reasoning=("Constraint-heavy problems benefit from QUBO."),
            )

        return AdaptiveSolverSelection(
            primary_solver="hybrid",
            solver_weights=(
                (
                    "qubo",
                    0.33,
                ),
                (
                    "annealing",
                    0.33,
                ),
                (
                    "tensor",
                    0.34,
                ),
            ),
            reasoning=("Balanced hybrid optimization."),
        )
