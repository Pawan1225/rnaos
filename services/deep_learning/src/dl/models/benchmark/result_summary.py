"""
RNAOS benchmark result summary model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ResultSummary:
    """
    Immutable benchmark summary.
    """

    best_method: str

    best_accuracy: float

    best_energy: float

    runtime_improvement: float

    summary_text: str

    key_findings: tuple[str, ...]
