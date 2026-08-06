"""
RNAOS machine learning model registry.
"""

from __future__ import annotations

from sklearn.ensemble import (
    RandomForestRegressor,
)
from sklearn.gaussian_process import (
    GaussianProcessRegressor,
)
from sklearn.linear_model import (
    BayesianRidge,
)
from sklearn.neighbors import (
    KNeighborsRegressor,
)
from sklearn.svm import (
    SVR,
)
from sklearn.tree import (
    DecisionTreeRegressor,
)

from ml.constants import (
    DEFAULT_RANDOM_SEED,
)

MODEL_REGISTRY = {
    "random_forest": lambda: RandomForestRegressor(
        random_state=DEFAULT_RANDOM_SEED,
    ),
    "decision_tree": lambda: DecisionTreeRegressor(
        random_state=DEFAULT_RANDOM_SEED,
    ),
    "knn": lambda: KNeighborsRegressor(),
    "svm": lambda: SVR(),
    "bayesian_regression": lambda: BayesianRidge(),
    "gaussian_process": lambda: GaussianProcessRegressor(),
}
