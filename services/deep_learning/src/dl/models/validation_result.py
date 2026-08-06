"""
RNAOS validation result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class ValidationResult:
    """
    Immutable validation execution result.
    """

    validation_loss: float

    validation_accuracy: float

    samples_evaluated: int

    success: bool
