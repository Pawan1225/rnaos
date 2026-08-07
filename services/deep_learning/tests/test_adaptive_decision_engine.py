"""
Tests for adaptive decision engine.
"""

from __future__ import annotations

from dl.models.optimization.decision_context import (
    DecisionContext,
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
from dl.optimization.solver_intelligence_registry import (
    SolverIntelligenceRegistry,
)


def test_adaptive_decision() -> None:
    """
    Decision engine selects the best solver.
    """

    registry = SolverRegistry(
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

    context = DecisionContext(
        problem_type="rna_folding",
        complexity=0.95,
        accuracy_requirement=0.98,
        resource_level=0.80,
    )

    engine = AdaptiveDecisionEngine()

    recommendation = engine.decide(
        context=context,
        registry=SolverIntelligenceRegistry(
            registry,
        ),
    )

    assert recommendation.solver == "ising"

    assert recommendation.confidence == 0.95

    assert recommendation.reasoning == "highest capability"
