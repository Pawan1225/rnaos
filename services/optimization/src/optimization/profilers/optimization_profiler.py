"""
Optimization Profiler

Coordinates optimization problem generation.
"""

from __future__ import annotations

from ai_intelligence.profilers.ai_profiler import AIProfile
from folding.profilers.folding_profiler import FoldingProfile

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
        folding_profile: FoldingProfile,
    ) -> OptimizationProfile:
        """
        Generate a complete optimization profile.

        Parameters
        ----------
        ai_profile : AIProfile
            AI-derived analysis and solver recommendations.

        folding_profile : FoldingProfile
            Biological RNA folding profile.
        """

        # ------------------------------------------------------------------
        # Biology-aware decision variables
        # ------------------------------------------------------------------
        variables = [
            DecisionVariable(
                name=f"x_{candidate.left}_{candidate.right}",
                variable_type=VariableType.BINARY,
            )
            for candidate in folding_profile.search_space.candidates
        ]

        # ------------------------------------------------------------------
        # Biology-aware optimization metadata
        # ------------------------------------------------------------------
        candidate_count = folding_profile.search_space.variable_count

        conflict_count = folding_profile.search_space.conflict_count

        density = conflict_count / max(candidate_count, 1)

        metadata = OptimizationMetadata(
            solver_hint=ai_profile.recommendation.solver,
            complexity_score=ai_profile.complexity.score,
            candidate_pair_count=candidate_count,
            conflict_count=conflict_count,
            search_space_density=density,
            mfe=folding_profile.thermodynamics.mfe,
            energy_gap=folding_profile.thermodynamics.energy_gap,
            tags=[
                "rna",
                "folding",
                "qubo",
                "biology-aware",
            ],
            extra={
                "sequence_length": (folding_profile.secondary_structure.length),
                "structure": (folding_profile.secondary_structure.dot_bracket),
                "estimated_qubo_size": candidate_count,
            },
        )

        # ------------------------------------------------------------------
        # Build optimization problem
        # ------------------------------------------------------------------
        problem = OptimizationProblem(
            variables=variables,
            objective=self.objective_generator.generate(
                folding_profile,
            ),
            constraints=self.constraint_generator.generate(
                folding_profile,
            ),
            metadata=metadata,
        )

        # ------------------------------------------------------------------
        # Validate
        # ------------------------------------------------------------------
        validation = self.validator.validate(problem)

        if not validation.is_valid:
            raise ValueError(f"Invalid optimization problem: {validation.errors}")

        # ------------------------------------------------------------------
        # Generate RNA Folding QUBO
        # ------------------------------------------------------------------
        qubo = self.qubo_generator.generate(
            folding_profile,
            [variable.name for variable in variables],
        )

        return OptimizationProfile(
            problem=problem,
            qubo=qubo,
        )
