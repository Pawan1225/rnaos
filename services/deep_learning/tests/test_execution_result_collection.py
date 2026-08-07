"""
Tests for execution result collection.
"""

from __future__ import annotations

from dl.models.optimization.execution_result_collection import (
    ExecutionResultCollection,
)
from dl.models.optimization.solver_result import (
    SolverResult,
)


def test_execution_result_collection() -> None:
    """
    Collection stores solver results.
    """

    result = SolverResult(
        solver_name="ising",
        solution=(
            1,
            0,
            1,
        ),
        energy=-45.2,
        iterations=100,
        converged=True,
    )

    collection = ExecutionResultCollection(
        collection_id=1,
        results=(result,),
        problem_id="rna_001",
        status="completed",
    )

    assert collection.collection_id == 1

    assert (
        len(
            collection.results,
        )
        == 1
    )

    assert collection.results[0].solver_name == ("ising")

    assert collection.status == ("completed")
