"""
Tests for solver orchestration engine.
"""

from __future__ import annotations

from dl.models.optimization.hybrid_strategy import (
    HybridStrategy,
)
from dl.models.optimization.orchestration_result import (
    OrchestrationResult,
)
from dl.models.optimization.solver_combination_rule import (
    SolverCombinationRule,
)
from dl.models.optimization.solver_execution_request import (
    SolverExecutionRequest,
)
from dl.models.optimization.strategy_configuration import (
    StrategyConfiguration,
)
from dl.optimization.solver_orchestration_engine import (
    SolverOrchestrationEngine,
)


def test_solver_orchestration() -> None:
    """
    Hybrid workflow executes.
    """

    strategy = HybridStrategy(
        configuration=StrategyConfiguration(
            strategy_name="hybrid",
            solvers=(
                "ising",
                "genetic",
                "tabu",
            ),
            execution_mode="sequential",
            objective="rna",
        ),
        rules=(
            SolverCombinationRule(
                primary_solver="ising",
                secondary_solver="genetic",
                refinement_solver="tabu",
                condition="complex",
            ),
        ),
        confidence=0.90,
    )

    request = SolverExecutionRequest(
        request_id=1,
        problem_type="rna",
        strategy_name="hybrid",
        priority=1,
    )

    engine = SolverOrchestrationEngine()

    result = engine.execute(
        request=request,
        strategy=strategy,
    )

    assert isinstance(
        result,
        OrchestrationResult,
    )

    assert result.selected_strategy == "hybrid"

    assert result.enabled_modules == (
        "ising",
        "genetic",
        "tabu",
    )

    assert result.confidence == 0.90
