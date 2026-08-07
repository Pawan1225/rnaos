"""
Tests for parallel solver coordinator.
"""

from __future__ import annotations

from dl.models.optimization.parallel_coordination_result import (
    ParallelCoordinationResult,
)
from dl.models.optimization.parallel_execution_task import (
    ParallelExecutionTask,
)
from dl.models.optimization.solver_execution_pool import (
    SolverExecutionPool,
)
from dl.optimization.parallel_solver_coordinator import (
    ParallelSolverCoordinator,
)


def test_parallel_solver_coordinator() -> None:
    """
    Parallel coordinator processes execution pool.
    """

    pool = SolverExecutionPool(
        tasks=(
            ParallelExecutionTask(
                task_id=1,
                solver_name="ising",
                priority=1,
                status="completed",
            ),
            ParallelExecutionTask(
                task_id=2,
                solver_name="genetic",
                priority=2,
                status="completed",
            ),
        ),
        capacity=2,
    )

    coordinator = ParallelSolverCoordinator()

    result = coordinator.coordinate(
        pool,
    )

    assert isinstance(
        result,
        ParallelCoordinationResult,
    )

    assert result.total_tasks == 2

    assert result.completed_tasks == 2

    assert result.executed_solvers == (
        "ising",
        "genetic",
    )

    assert result.success is True
