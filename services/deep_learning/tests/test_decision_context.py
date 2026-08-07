"""
Tests for decision context model.
"""

from __future__ import annotations

from dl.models.optimization.decision_context import (
    DecisionContext,
)


def test_decision_context() -> None:
    """
    Decision context can be created.
    """

    context = DecisionContext(
        problem_type="rna_folding",
        complexity=0.95,
        accuracy_requirement=0.98,
        resource_level=0.80,
    )

    assert context.problem_type == "rna_folding"

    assert context.complexity == 0.95

    assert context.accuracy_requirement == 0.98

    assert context.resource_level == 0.80
