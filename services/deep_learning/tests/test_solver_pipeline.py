"""
Tests for solver pipeline model.
"""

from __future__ import annotations

from dl.models.optimization.solver_pipeline import (
    SolverPipeline,
)


def test_solver_pipeline_creation() -> None:
    """
    Pipeline can be created.
    """

    pipeline = SolverPipeline(
        pipeline_id=1,
        solvers=(
            "ising",
            "genetic",
            "tabu",
        ),
        stages=3,
    )

    assert pipeline.pipeline_id == 1

    assert pipeline.stages == 3

    assert (
        len(
            pipeline.solvers,
        )
        == 3
    )

    assert pipeline.solvers == (
        "ising",
        "genetic",
        "tabu",
    )
