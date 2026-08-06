"""
RNAOS trained model.
"""

from __future__ import annotations

from dataclasses import dataclass

from sklearn.base import (
    BaseEstimator,
)


@dataclass(slots=True, frozen=True)
class TrainedModel:
    """
    Immutable trained model.
    """

    model_name: str

    estimator: BaseEstimator

    metric_name: str

    metric_value: float

    training_time: float

    feature_count: int

    sample_count: int

    training_status: str

    @property
    def is_trained(
        self,
    ) -> bool:
        """
        Whether the estimator exists.
        """
        return self.estimator is not None
