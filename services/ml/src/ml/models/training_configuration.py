"""
RNAOS training configuration model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class TrainingConfiguration:
    """
    Immutable model training configuration.

    Defines the configuration required to train
    exactly one machine learning model.
    """

    model_name: str

    cross_validation_folds: int

    random_seed: int

    shuffle: bool
