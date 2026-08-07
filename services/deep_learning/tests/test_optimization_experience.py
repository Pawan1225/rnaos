"""
Tests for optimization experience model.
"""

from __future__ import annotations

from dl.models.optimization.optimization_experience import (
    OptimizationExperience,
)


def test_optimization_experience_creation() -> None:
    """
    Experience can be created.
    """

    experience = OptimizationExperience(
        experience_id=1,
        solver_name="genetic",
        problem_type="rna_folding",
        fitness=0.95,
        execution_time=1.2,
    )

    assert experience.experience_id == 1

    assert experience.solver_name == "genetic"

    assert experience.problem_type == "rna_folding"

    assert experience.fitness == 0.95

    assert experience.execution_time == 1.2
