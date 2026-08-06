"""
RNAOS machine learning constants.
"""

from __future__ import annotations

SUPPORTED_MODELS = (
    "random_forest",
    "decision_tree",
    "knn",
    "svm",
    "bayesian_regression",
    "gaussian_process",
)

DEFAULT_RANDOM_SEED = 42

DEFAULT_CROSS_VALIDATION_FOLDS = 5

DEFAULT_SHUFFLE = True

DEFAULT_SCORING_METRIC = "r2"

DEFAULT_TOP_K_FEATURES = 10
