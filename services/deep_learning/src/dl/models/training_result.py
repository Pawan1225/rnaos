"""
RNAOS training result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class TrainingResult:
    """
    Immutable training execution result.
    """

    epochs_completed: int

    final_loss: float

    training_history: tuple[float, ...]

    success: bool
