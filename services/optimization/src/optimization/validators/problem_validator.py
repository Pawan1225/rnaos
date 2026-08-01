"""
Optimization Problem Validator.

Validates OptimizationProblem instances before they are
translated or submitted to a solver.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from optimization.models.optimization_problem import OptimizationProblem


@dataclass(slots=True)
class ValidationResult:
    """Result of optimization problem validation."""

    is_valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


class OptimizationProblemValidator:
    """Validates optimization problems."""

    def validate(
        self,
        problem: OptimizationProblem,
    ) -> ValidationResult:
        """Validate an optimization problem."""

        errors: list[str] = []
        warnings: list[str] = []

        if not problem.variables:
            errors.append("Optimization problem contains no variables.")

        if problem.objective.expression.strip() == "":
            errors.append("Objective expression cannot be empty.")

        if problem.metadata.complexity_score < 0:
            errors.append("Complexity score must be non-negative.")

        variable_names = [variable.name for variable in problem.variables]

        if len(variable_names) != len(set(variable_names)):
            errors.append("Duplicate variable names detected.")

        if problem.constraint_count == 0:
            warnings.append("Problem contains no constraints.")

        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
        )
