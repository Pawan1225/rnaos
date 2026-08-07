"""
Tests for adaptive controller engine.
"""

from __future__ import annotations

from dl.models.optimization.controller_decision import (
    ControllerDecision,
)
from dl.models.optimization.solver_recommendation import (
    SolverRecommendation,
)
from dl.optimization.adaptive_controller_engine import (
    AdaptiveControllerEngine,
)


def test_adaptive_controller_decision() -> None:
    """
    Controller creates a learned decision.
    """

    engine = AdaptiveControllerEngine()

    recommendation = SolverRecommendation(
        solver="genetic",
        confidence=0.92,
        reasoning="Highest historical reward.",
    )

    decision = engine.decide(
        problem_type="rna_folding",
        recommendation=recommendation,
    )

    assert isinstance(
        decision,
        ControllerDecision,
    )

    assert decision.problem_type == "rna_folding"

    assert decision.selected_solver == "genetic"

    assert decision.confidence == 0.92

    assert decision.learned is True
