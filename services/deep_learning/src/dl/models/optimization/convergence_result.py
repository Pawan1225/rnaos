"""
RNAOS convergence result models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ConvergenceResult:
    """
    Immutable convergence result.
    """

    converged: bool

    improvement: float
