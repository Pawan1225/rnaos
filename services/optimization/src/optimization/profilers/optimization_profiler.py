"""
Optimization Profiler

Coordinates optimization problem generation.
"""

from __future__ import annotations

from ai_intelligence.profilers.ai_profiler import AIProfile

from optimization.constraints.constraint_generator import (
    ConstraintGenerator,
)
from optimization.generators.qubo_generator import (
    QUBOGenerator,
)
from optimization.models.optimization_problem import (
    DecisionVariable,
    OptimizationMetadata,
    OptimizationProblem,
    OptimizationProfile,
    VariableType,
)
from optimization.objectives.objective_generator import (
    ObjectiveFunctionGenerator,
)
from optimization.validators.problem_validator import (
    OptimizationProblemValidator,
)


class OptimizationProfiler:
    """Coordinates optimization generation."""

    def __init__(self) -> None:
        self.objective_generator = ObjectiveFunctionGenerator()
        self.constraint_generator = ConstraintGenerator()
        self.validator = OptimizationProblemValidator()
        self.qubo_generator = QUBOGenerator()

    def profile(
        self,
        ai_profile: AIProfile,
    ) -> OptimizationProfile:
        """Generate a complete optimization profile."""

        sequence_length = int(ai_profile.features.values[0])

        variables = [
            DecisionVariable(
                name=f"x{i}",
                variable_type=VariableType.BINARY,
            )
            for i in range(sequence_length)
        ]

        problem = OptimizationProblem(
            variables=variables,
            objective=self.objective_generator.generate(ai_profile),
            constraints=self.constraint_generator.generate(ai_profile),
            metadata=OptimizationMetadata(
                solver_hint=ai_profile.recommendation.solver,
                complexity_score=ai_profile.complexity.score,
            ),
        )

        validation = self.validator.validate(problem)

        if not validation.is_valid:
            raise ValueError(f"Invalid optimization problem: {validation.errors}")

        qubo = self.qubo_generator.generate(problem)

        return OptimizationProfile(
            problem=problem,
            qubo=qubo,
        )
