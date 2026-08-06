"""
RNAOS cross-validation utilities.
"""

from __future__ import annotations

from collections.abc import Sequence

from sklearn.base import BaseEstimator
from sklearn.model_selection import cross_val_score


def evaluate_model(
    model: BaseEstimator,
    features: Sequence[Sequence[float]],
    targets: Sequence[float],
    folds: int,
) -> float:
    """
    Evaluate a model using cross-validation.

    Parameters
    ----------
    model
        Machine learning model.

    features
        Feature matrix.

    targets
        Target values.

    folds
        Number of cross-validation folds.

    Returns
    -------
    float
        Mean cross-validation score.
    """
    scores = cross_val_score(
        estimator=model,
        X=features,
        y=targets,
        cv=folds,
    )

    return float(
        scores.mean(),
    )
