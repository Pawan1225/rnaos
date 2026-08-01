"""
Genetic Algorithm Solver.
"""

from __future__ import annotations

import random

from optimization.models.optimization_problem import (
    OptimizationProblem,
)

from solver_portfolio.base.base_solver import (
    BaseSolver,
    SolverResult,
)


class GeneticSolver(BaseSolver):
    """Binary Genetic Algorithm."""

    name = "genetic"

    def __init__(
        self,
        population_size: int = 30,
        generations: int = 50,
        mutation_rate: float = 0.05,
    ) -> None:
        """Initialize the genetic algorithm solver."""

        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate

    def _fitness(
        self,
        chromosome: list[int],
    ) -> float:
        """Compute the fitness of a chromosome."""

        return float(sum(chromosome))

    def _tournament(
        self,
        population: list[list[int]],
    ) -> list[int]:
        """Perform tournament selection."""

        candidate_a = random.choice(population)
        candidate_b = random.choice(population)

        if self._fitness(candidate_a) >= self._fitness(candidate_b):
            return candidate_a

        return candidate_b

    def solve(
        self,
        problem: OptimizationProblem,
    ) -> SolverResult:
        """Solve an optimization problem using a genetic algorithm."""

        def _solve() -> SolverResult:
            n = problem.variable_count

            population = [
                [random.randint(0, 1) for _ in range(n)] for _ in range(self.population_size)
            ]

            for _ in range(self.generations):
                population.sort(
                    key=self._fitness,
                    reverse=True,
                )

                # Elitism: preserve the best solution.
                new_population = [
                    population[0].copy(),
                ]

                while len(new_population) < self.population_size:
                    parent1 = random.choice(population[:10])
                    parent2 = random.choice(population[:10])

                    # One-point crossover requires at least two genes.
                    if n > 1:
                        crossover_point = random.randint(
                            1,
                            n - 1,
                        )

                        child = parent1[:crossover_point] + parent2[crossover_point:]
                    else:
                        child = parent1.copy()

                    # Bit-flip mutation.
                    for i in range(n):
                        if random.random() < self.mutation_rate:
                            child[i] ^= 1

                    new_population.append(child)

                population = new_population

            best = max(
                population,
                key=self._fitness,
            )

            solution = {
                variable.name: float(best[i]) for i, variable in enumerate(problem.variables)
            }

            return SolverResult(
                solver_name=self.name,
                objective_value=self._fitness(best),
                solution=solution,
                runtime_seconds=0.0,
                success=True,
                metadata={
                    "population_size": self.population_size,
                    "generations": self.generations,
                    "mutation_rate": self.mutation_rate,
                },
            )

        result, runtime = self.measure_runtime(_solve)

        result.runtime_seconds = runtime

        return result
