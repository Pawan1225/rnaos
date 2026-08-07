"""
RNAOS orchestration metrics model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class OrchestrationMetrics:
    """
    Immutable orchestration metrics.
    """

    executed_solvers: int

    successful_executions: int

    average_confidence: float

    parallel_tasks: int
