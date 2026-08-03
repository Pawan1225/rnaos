"""
Shared solver component container.
"""

from __future__ import annotations

from dataclasses import dataclass

from solver.utils import (
    ExponentialCoolingSchedule,
    MetropolisAcceptanceCriterion,
    NeighbourGenerator,
    QUBOObjectiveEvaluator,
    RandomSolutionGenerator,
)


@dataclass(slots=True)
class SolverComponents:
    """Container for reusable solver components."""

    objective: QUBOObjectiveEvaluator

    random_solution: RandomSolutionGenerator

    neighbours: NeighbourGenerator

    acceptance: MetropolisAcceptanceCriterion

    cooling: ExponentialCoolingSchedule
