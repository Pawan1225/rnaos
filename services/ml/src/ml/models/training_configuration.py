"""
RNAOS training configuration model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class TrainingConfiguration:
    """
    Immutable AutoML training configuration.
    """

    model_names: tuple[str, ...]

    cross_validation_folds: int

    random_seed: int

    shuffle: bool

    @property
    def model_count(
        self,
    ) -> int:
        """
        Number of configured models.
        """
        return len(
            self.model_names,
        )
