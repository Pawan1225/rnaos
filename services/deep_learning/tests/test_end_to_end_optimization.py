"""
End-to-end RNAOS optimization validation.
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


def test_end_to_end_optimization() -> None:
    """
    Complete RNAOS optimization pipeline works.
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
            SolverEntry(
                solver_name="tabu",
                category="local_search",
                capability_score=0.85,
                available=True,
            ),
        ),
        total_solvers=3,
    )

    registry = SolverIntelligenceRegistry(
        solver_registry,
    )

    controller = GlobalOptimizationController(
        decision_engine=AdaptiveDecisionEngine(),
        registry=registry,
    )

    request = GlobalOptimizationRequest(
        request_id=100,
        problem_type="rna_structure_prediction",
        complexity=0.98,
        priority=1,
        accuracy_target=0.99,
    )

    result = controller.optimize(
        request,
    )

    assert result.execution_id == 100

    assert result.selected_solver == "ising"

    assert result.strategy == "adaptive"

    assert result.status == "completed"
