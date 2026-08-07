"""
Tests for solver execution pool.
"""

from __future__ import annotations

from dl.models.optimization.parallel_execution_task import (
    ParallelExecutionTask,
)
from dl.models.optimization.solver_execution_pool import (
    SolverExecutionPool,
)


def test_solver_execution_pool() -> None:
    """
    Solver execution pool stores tasks.
    """

    pool = SolverExecutionPool(
        tasks=(
            ParallelExecutionTask(
                task_id=1,
                solver_name="ising",
                priority=1,
                status="pending",
            ),
            ParallelExecutionTask(
                task_id=2,
                solver_name="genetic",
                priority=2,
                status="pending",
            ),
            ParallelExecutionTask(
                task_id=3,
                solver_name="pso",
                priority=3,
                status="pending",
            ),
        ),
        capacity=3,
    )

    assert (
        len(
            pool.tasks,
        )
        == 3
    )

    assert pool.capacity == 3

    assert pool.tasks[0].solver_name == "ising"

    assert pool.tasks[1].solver_name == "genetic"

    assert pool.tasks[2].solver_name == "pso"
