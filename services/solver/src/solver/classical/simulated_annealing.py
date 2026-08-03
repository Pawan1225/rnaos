"""
Simulated Annealing Solver.
"""

from __future__ import annotations

import time

from optimization.models.optimization_problem import QUBOProblem

from solver.base.base_solver import BaseSolver
from solver.components import SolverComponents
from solver.evaluation import QUBOEvaluator
from solver.models import (
    SolverCapabilities,
    SolverFamily,
    SolverResult,
)
from solver.utils import (
    ExponentialCoolingSchedule,
    MetropolisAcceptanceCriterion,
    NeighbourGenerator,
    QUBOObjectiveEvaluator,
    RandomSolutionGenerator,
)


class SimulatedAnnealingSolver(BaseSolver):
    """Classical Simulated Annealing solver."""

    def __init__(
        self,
        *,
        initial_temperature: float = 100.0,
        cooling_rate: float = 0.995,
        minimum_temperature: float = 1e-3,
        max_iterations: int = 1_000,
    ) -> None:
        """Initialize the Simulated Annealing solver."""

        self._components = SolverComponents(
            objective=QUBOObjectiveEvaluator(),
            random_solution=RandomSolutionGenerator(),
            neighbours=NeighbourGenerator(),
            acceptance=MetropolisAcceptanceCriterion(),
            cooling=ExponentialCoolingSchedule(
                initial_temperature=initial_temperature,
                cooling_rate=cooling_rate,
                minimum_temperature=minimum_temperature,
            ),
        )

        self._max_iterations = max_iterations

    @property
    def name(self) -> str:
        """Return the solver name."""

        return "Simulated Annealing"

    @property
    def capabilities(self) -> SolverCapabilities:
        """Return the solver capabilities."""

        return SolverCapabilities(
            solver_family=SolverFamily.CLASSICAL,
            supports_sparse_qubo=True,
            supports_dense_qubo=True,
            supports_binary_variables=True,
            supports_continuous_variables=False,
            deterministic=False,
            parallel=False,
            gpu_accelerated=False,
            quantum=False,
            hybrid=False,
            max_problem_size=5_000,
        )

    @property
    def max_iterations(self) -> int:
        """Return the maximum number of iterations."""

        return self._max_iterations

    @property
    def cooling_schedule(self) -> ExponentialCoolingSchedule:
        """Return the cooling schedule."""

        return self._components.cooling

    @property
    def components(self) -> SolverComponents:
        """Return the shared solver components."""

        return self._components

    def solve(
        self,
        problem: QUBOProblem,
    ) -> SolverResult:
        """Solve a QUBO problem using Simulated Annealing."""

        start_time = time.perf_counter()

        current_solution = self.components.random_solution.generate(
            problem,
        )

        current_objective = QUBOEvaluator.evaluate(
            problem,
            current_solution,
        )

        best_solution = current_solution.copy()
        best_objective = current_objective

        for iteration in range(self.max_iterations):
            temperature = self.components.cooling.temperature(
                iteration,
            )

            candidate_solution = self.components.neighbours.flip_random_bit(
                current_solution,
            )

            candidate_objective = QUBOEvaluator.evaluate(
                problem,
                candidate_solution,
            )

            accepted = self.components.acceptance.accept(
                current_objective=current_objective,
                candidate_objective=candidate_objective,
                temperature=temperature,
            )

            if accepted:
                current_solution = candidate_solution
                current_objective = candidate_objective

                if current_objective < best_objective:
                    best_solution = current_solution.copy()
                    best_objective = current_objective

        runtime = time.perf_counter() - start_time

        return SolverResult(
            solver_name=self.name,
            objective_value=best_objective,
            solution=best_solution,
            runtime_seconds=runtime,
            iterations=self.max_iterations,
        )
