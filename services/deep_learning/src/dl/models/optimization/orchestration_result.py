"""
RNAOS orchestration result models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class OrchestrationResult:
    """
    Immutable orchestration result.
    """

    selected_strategy: str

    enabled_modules: tuple[str, ...]

    confidence: float
