"""
RNAOS trained model.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True, frozen=True)
class TrainedModel:
    """
    Immutable trained model.
    """

    model_name: str

    estimator: Any

    score: float

    training_time: float

    feature_count: int

    sample_count: int

    @property
    def is_trained(
        self,
    ) -> bool:
        """
        Whether the estimator exists.
        """
        return self.estimator is not None
