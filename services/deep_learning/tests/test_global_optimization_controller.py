"""
Tests for global optimization controller.
"""

from __future__ import annotations

from dl.models.optimization.global_optimization_request import (
    GlobalOptimizationRequest,
)
from dl.models.optimization.solver_entry import (
    SolverEntry,
)
from dl.models.optimization.solver_registry import (
    SolverRegistry,
)
from dl.optimization.adaptive_decision_engine import (
    AdaptiveDecisionEngine,
)
from dl.optimization.global_optimization_controller import (
    GlobalOptimizationController,
)
from dl.optimization.solver_intelligence_registry import (
    SolverIntelligenceRegistry,
)


def test_global_optimization_controller() -> None:
    """
    Global optimization controller selects the best solver.
    """

    solver_registry = SolverRegistry(
        solvers=(
            SolverEntry(
                solver_name="ising",
                category="quantum",
                capability_score=0.95,
                available=True,
            ),
            SolverEntry(
                solver_name="genetic",
                category="evolutionary",
                capability_score=0.90,
                available=True,
            ),
        ),
        total_solvers=2,
    )

    registry = SolverIntelligenceRegistry(
        solver_registry,
    )

    controller = GlobalOptimizationController(
        decision_engine=AdaptiveDecisionEngine(),
        registry=registry,
    )

    request = GlobalOptimizationRequest(
        request_id=1,
        problem_type="rna_folding",
        complexity=0.95,
        priority=1,
        accuracy_target=0.98,
    )

    result = controller.optimize(
        request,
    )

    assert result.execution_id == 1

    assert result.selected_solver == "ising"

    assert result.strategy == "adaptive"

    assert result.status == "completed"
