"""
RNAOS deep learning training configuration.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    slots=True,
    frozen=True,
)
class TrainingConfiguration:
    """
    Immutable deep learning training settings.
    """

    epochs: int = 10

    batch_size: int = 32

    learning_rate: float = 0.001

    optimizer: str = "adam"

    validation_split: float = 0.2

    random_seed: int = 42

    checkpoint_frequency: int = 1
