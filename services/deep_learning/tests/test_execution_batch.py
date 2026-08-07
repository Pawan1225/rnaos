"""
Tests for execution batch model.
"""

from __future__ import annotations

from dl.models.optimization.execution_batch import (
    ExecutionBatch,
)
from dl.models.optimization.solver_execution import (
    SolverExecution,
)


def test_execution_batch() -> None:
    """
    Batch stores solver executions.
    """

    execution = SolverExecution(
        execution_id=1,
        solver_name="ising",
        problem_id="rna_001",
        parameters=("iterations=100",),
        status="pending",
    )

    batch = ExecutionBatch(
        batch_id=1,
        executions=(execution,),
        problem_id="rna_001",
        status="pending",
    )

    assert batch.batch_id == 1

    assert len(batch.executions) == 1

    assert batch.executions[0] == execution

    assert batch.problem_id == "rna_001"

    assert batch.status == "pending"
