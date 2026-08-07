"""
RNAOS solver orchestration engine.
"""

from __future__ import annotations

from dl.models.optimization.hybrid_strategy import (
    HybridStrategy,
)
from dl.models.optimization.orchestration_result import (
    OrchestrationResult,
)
from dl.models.optimization.solver_execution_request import (
    SolverExecutionRequest,
)


class SolverOrchestrationEngine:
    """
    Executes hybrid solver strategies.
    """

    def execute(
        self,
        request: SolverExecutionRequest,
        strategy: HybridStrategy,
    ) -> OrchestrationResult:
        """
        Execute a hybrid solver workflow.
        """

        return OrchestrationResult(
            selected_strategy=request.strategy_name,
            enabled_modules=(strategy.configuration.solvers),
            confidence=strategy.confidence,
        )
