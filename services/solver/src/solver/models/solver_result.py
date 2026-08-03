"""
Solver Result.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class SolverResult:
    """Result returned by every solver."""

    solver_name: str

    objective_value: float

    solution: list[int]

    runtime_seconds: float

    iterations: int

    metadata: dict[str, object] = field(default_factory=dict)

    @property
    def variable_count(self) -> int:
        """Return the number of decision variables."""
        return len(self.solution)
