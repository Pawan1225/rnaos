"""
RNAOS AutoML configuration model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class AutoMLConfiguration:
    """
    Immutable AutoML configuration.

    Defines the set of models that should be trained
    and compared by the AutoML engine.
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
