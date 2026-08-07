"""
RNAOS global optimization controller.
"""

from __future__ import annotations

from dl.models.optimization.decision_context import (
    DecisionContext,
)
from dl.models.optimization.global_optimization_request import (
    GlobalOptimizationRequest,
)
from dl.models.optimization.global_optimization_result import (
    GlobalOptimizationResult,
)
from dl.optimization.adaptive_decision_engine import (
    AdaptiveDecisionEngine,
)
from dl.optimization.solver_intelligence_registry import (
    SolverIntelligenceRegistry,
)


class GlobalOptimizationController:
    """
    Coordinates the complete RNAOS optimization workflow.
    """

    def __init__(
        self,
        decision_engine: AdaptiveDecisionEngine,
        registry: SolverIntelligenceRegistry,
    ) -> None:
        self._decision_engine = decision_engine
        self._registry = registry

    def optimize(
        self,
        request: GlobalOptimizationRequest,
    ) -> GlobalOptimizationResult:
        """
        Execute the global optimization workflow.
        """

        context = DecisionContext(
            problem_type=request.problem_type,
            complexity=request.complexity,
            accuracy_requirement=request.accuracy_target,
            resource_level=1.0,
        )

        recommendation = self._decision_engine.decide(
            context=context,
            registry=self._registry,
        )

        return GlobalOptimizationResult(
            execution_id=request.request_id,
            selected_solver=recommendation.solver,
            strategy="adaptive",
            status="completed",
        )
