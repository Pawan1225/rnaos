"""
Tests for optimization stage.
"""

from __future__ import annotations

from dl.models.optimization.optimization_stage import (
    OptimizationStage,
)


def test_optimization_stage() -> None:
    """
    Stage can be created.
    """

    stage = OptimizationStage(
        stage_id=1,
        name="exploration",
        solver_name="genetic",
        priority=1,
        status="pending",
    )

    assert stage.stage_id == 1

    assert stage.name == ("exploration")

    assert stage.solver_name == ("genetic")

    assert stage.priority == 1

    assert stage.status == ("pending")
