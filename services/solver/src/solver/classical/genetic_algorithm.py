"""
Genetic Algorithm Solver.
"""

from __future__ import annotations

import time

from optimization.models.optimization_problem import QUBOProblem

from solver.base.base_solver import BaseSolver
from solver.evaluation import QUBOEvaluator
from solver.models import (
    SolverCapabilities,
    SolverFamily,
    SolverResult,
)
from solver.utils import (
    BitFlipMutation,
    RandomSolutionGenerator,
    SinglePointCrossover,
    TournamentSelection,
)


class GeneticAlgorithmSolver(BaseSolver):
    """Classical Genetic Algorithm solver."""

    def __init__(
        self,
        *,
        population_size: int = 50,
        generations: int = 100,
        mutation_rate: float = 0.05,
    ) -> None:
        """Initialize the Genetic Algorithm solver."""

        self._population_size = population_size
        self._generations = generations
        self._mutation_rate = mutation_rate

        self._random_solution = RandomSolutionGenerator()

    @property
    def name(self) -> str:
        """Return the solver name."""

        return "Genetic Algorithm"

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
    def population_size(self) -> int:
        """Return the population size."""

        return self._population_size

    @property
    def generations(self) -> int:
        """Return the number of generations."""

        return self._generations

    @property
    def mutation_rate(self) -> float:
        """Return the mutation rate."""

        return self._mutation_rate

    def solve(
        self,
        problem: QUBOProblem,
    ) -> SolverResult:
        """Solve a QUBO problem using a Genetic Algorithm."""

        start_time = time.perf_counter()

        population = [self._random_solution.generate(problem) for _ in range(self.population_size)]

        best_solution = min(
            population,
            key=lambda solution: QUBOEvaluator.evaluate(
                problem,
                solution,
            ),
        ).copy()

        best_objective = QUBOEvaluator.evaluate(
            problem,
            best_solution,
        )

        score = lambda solution: QUBOEvaluator.evaluate(  # noqa: E731
            problem,
            solution,
        )

        for _ in range(self.generations):
            next_population: list[list[int]] = []

            while len(next_population) < self.population_size:
                parent_one = TournamentSelection.select(
                    population,
                    score,
                )

                parent_two = TournamentSelection.select(
                    population,
                    score,
                )

                child = SinglePointCrossover.crossover(
                    parent_one,
                    parent_two,
                )

                child = BitFlipMutation.mutate(
                    child,
                    self.mutation_rate,
                )

                next_population.append(child)

            population = next_population

            generation_best = min(
                population,
                key=score,
            )

            generation_objective = score(
                generation_best,
            )

            if generation_objective < best_objective:
                best_solution = generation_best.copy()
                best_objective = generation_objective

        runtime = time.perf_counter() - start_time

        return SolverResult(
            solver_name=self.name,
            objective_value=best_objective,
            solution=best_solution,
            runtime_seconds=runtime,
            iterations=self.generations,
        )
