"""
RNAOS AI feature vector model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class FeatureVector:
    """
    Immutable AI feature vector.

    This model stores a deterministic numerical
    representation of a biological intelligence profile.
    The feature vector serves as the common input for
    machine learning, deep learning, quantum machine
    learning, and optimization engines.
    """

    feature_names: tuple[str, ...]

    values: tuple[float, ...]

    dimension: int

    @property
    def size(
        self,
    ) -> int:
        """
        Number of features.
        """
        return self.dimension
