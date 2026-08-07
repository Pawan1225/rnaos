"""
RNAOS solver execution manager.
"""

from __future__ import annotations

from dl.models.optimization.execution_batch import (
    ExecutionBatch,
)
from dl.models.optimization.execution_result_collection import (
    ExecutionResultCollection,
)
from dl.optimization.runtime.solver_runtime import (
    SolverRuntime,
)


class SolverExecutionManager:
    """
    Manages multiple solver executions.
    """

    def __init__(
        self,
        runtime: SolverRuntime,
    ) -> None:
        self._runtime = runtime

    def execute(
        self,
        batch: ExecutionBatch,
    ) -> ExecutionResultCollection:
        """
        Execute all solver requests.
        """

        results = tuple(
            self._runtime.execute(
                execution,
            )
            for execution in batch.executions
        )

        return ExecutionResultCollection(
            collection_id=batch.batch_id,
            results=results,
            problem_id=batch.problem_id,
            status="completed",
        )
