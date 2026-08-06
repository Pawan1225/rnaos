"""
RNAOS machine learning training utilities.
"""

from __future__ import annotations

from ml.model_registry import (
    MODEL_REGISTRY,
)
from sklearn.base import BaseEstimator


def create_model(
    model_name: str,
) -> BaseEstimator:
    """
    Create a machine learning model from the registry.

    Parameters
    ----------
    model_name
        Name of the registered machine learning model.

    Returns
    -------
    BaseEstimator
        Instantiated machine learning model.

    Raises
    ------
    ValueError
        If the requested model is not registered.
    """
    try:
        factory = MODEL_REGISTRY[model_name]
    except KeyError as exc:
        raise ValueError(f"Unsupported model: {model_name}") from exc

    return factory()


def train_model(
    model: BaseEstimator,
    features: list[list[float]],
    targets: list[float],
) -> BaseEstimator:
    """
    Train a machine learning model.

    Parameters
    ----------
    model
        Machine learning model.

    features
        Training feature matrix.

    targets
        Training target values.

    Returns
    -------
    BaseEstimator
        Trained machine learning model.
    """
    model.fit(
        features,
        targets,
    )

    return model
