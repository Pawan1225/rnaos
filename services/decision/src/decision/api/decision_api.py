"""
Unified Decision Intelligence API.
"""

from __future__ import annotations

from decision.explainers import (
    FoldingExplainer,
    OptimizationExplainer,
    RuleBasedSolverExplainer,
)
from decision.graph import (
    DecisionGraph,
    DecisionNode,
)


class DecisionAPI:
    """
    Unified public interface for the RNAOS Decision Intelligence layer.

    This API provides a single entry point for generating solver,
    optimization, and RNA folding explanations while also supporting
    construction of a complete decision graph.
    """

    def __init__(self) -> None:
        self.solver = RuleBasedSolverExplainer()

        self.optimization = OptimizationExplainer()

        self.folding = FoldingExplainer()

    def explain_solver(
        self,
        *args,
        **kwargs,
    ):
        """Generate a solver explanation."""

        return self.solver.explain(
            *args,
            **kwargs,
        )

    def explain_optimization(
        self,
        problem,
    ):
        """Generate an optimization explanation."""

        return self.optimization.explain(
            problem,
        )

    def explain_folding(
        self,
        folding,
    ):
        """Generate an RNA folding explanation."""

        return self.folding.explain(
            folding,
        )

    def build_graph(
        self,
        solver_explanation,
        optimization_explanation,
        folding_explanation,
    ) -> DecisionGraph:
        """
        Build a reasoning graph linking all generated explanations.
        """

        graph = DecisionGraph()

        graph.add_node(
            DecisionNode(
                identifier="folding",
                explanation=folding_explanation,
            )
        )

        graph.add_node(
            DecisionNode(
                identifier="optimization",
                explanation=optimization_explanation,
            )
        )

        graph.add_node(
            DecisionNode(
                identifier="solver",
                explanation=solver_explanation,
            )
        )

        graph.add_edge(
            "folding",
            "optimization",
            "produces",
        )

        graph.add_edge(
            "optimization",
            "solver",
            "optimized_by",
        )

        return graph
