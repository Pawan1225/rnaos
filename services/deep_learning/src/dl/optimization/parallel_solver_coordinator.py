"""
RNAOS parallel solver coordinator.
"""

from __future__ import annotations

from dl.models.optimization.parallel_coordination_result import (
    ParallelCoordinationResult,
)
from dl.models.optimization.solver_execution_pool import (
    SolverExecutionPool,
)


class ParallelSolverCoordinator:
    """
    Coordinates parallel solver execution.
    """

    def coordinate(
        self,
        pool: SolverExecutionPool,
    ) -> ParallelCoordinationResult:
        """
        Coordinate execution of all solver tasks.
        """

        executed_solvers = tuple(task.solver_name for task in pool.tasks)

        completed_tasks = sum(task.status == "completed" for task in pool.tasks)

        return ParallelCoordinationResult(
            total_tasks=len(pool.tasks),
            completed_tasks=completed_tasks,
            executed_solvers=executed_solvers,
            success=completed_tasks == len(pool.tasks),
        )
