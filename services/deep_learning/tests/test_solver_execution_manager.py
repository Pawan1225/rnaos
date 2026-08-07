"""
Tests for solver execution manager.
"""

from __future__ import annotations

from dl.models.optimization.execution_batch import (
    ExecutionBatch,
)
from dl.models.optimization.execution_result_collection import (
    ExecutionResultCollection,
)
from dl.models.optimization.solver_execution import (
    SolverExecution,
)
from dl.optimization.runtime.execution_manager import (
    SolverExecutionManager,
)
from dl.optimization.runtime.solver_runtime import (
    SolverRuntime,
)


def test_solver_execution_manager() -> None:
    """
    Manager executes multiple solver requests.
    """

    batch = ExecutionBatch(
        batch_id=1,
        executions=(
            SolverExecution(
                execution_id=1,
                solver_name="ising",
                problem_id="rna_001",
                parameters=("iterations=100",),
                status="pending",
            ),
            SolverExecution(
                execution_id=2,
                solver_name="annealing",
                problem_id="rna_001",
                parameters=("temperature=100",),
                status="pending",
            ),
        ),
        problem_id="rna_001",
        status="pending",
    )

    manager = SolverExecutionManager(
        SolverRuntime(),
    )

    collection = manager.execute(
        batch,
    )

    assert isinstance(
        collection,
        ExecutionResultCollection,
    )

    assert (
        len(
            collection.results,
        )
        == 2
    )

    assert collection.results[0].solver_name == ("ising")

    assert collection.results[1].solver_name == ("annealing")

    assert collection.status == "completed"
