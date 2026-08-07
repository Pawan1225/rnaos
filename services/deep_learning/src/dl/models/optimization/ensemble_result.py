"""
RNAOS optimization ensemble models.
"""

from __future__ import annotations

from dataclasses import dataclass

from dl.models.optimization.solver_candidate import (
    SolverCandidate,
)


@dataclass(
    slots=True,
    frozen=True,
)
class EnsembleResult:
    """
    Immutable ensemble optimization result.
    """

    selected_solver: str | None = None

    energy: float | None = None

    candidate_count: int = 0

    candidates: tuple[SolverCandidate, ...] = ()

    selected_candidate: SolverCandidate | None = None

    consensus_score: float = 0.0

    confidence: float = 0.0

    status: str = "completed"
