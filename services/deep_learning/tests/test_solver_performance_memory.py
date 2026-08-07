"""
Tests for solver performance memory.
"""

from __future__ import annotations

from dl.models.optimization.optimization_experience import (
    OptimizationExperience,
)
from dl.models.optimization.solver_performance_memory import (
    SolverPerformanceMemory,
)
from dl.optimization.solver_performance_memory import (
    SolverPerformanceMemoryEngine,
)


def test_solver_memory() -> None:
    """
    Experiences are stored.
    """

    memory = SolverPerformanceMemory(
        experiences=(),
    )

    experience = OptimizationExperience(
        experience_id=1,
        solver_name="genetic",
        problem_type="rna",
        fitness=0.95,
        execution_time=1.0,
    )

    engine = SolverPerformanceMemoryEngine()

    updated = engine.add(
        memory,
        experience,
    )

    assert engine.size(updated) == 1

    assert updated.experiences[0] == experience
