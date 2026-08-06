"""
RNAOS feature selection engine.
"""

from __future__ import annotations

from ai.models.feature_vector import (
    FeatureVector,
)
from ml.models.selected_feature_set import (
    SelectedFeatureSet,
)
from ml.utils.feature_selection import (
    select_top_features,
    validate_top_k,
    variance_scores,
)


class FeatureSelectionEngine:
    """
    Select the most informative AI features for
    downstream machine learning.
    """

    def analyze(
        self,
        feature_vector: FeatureVector,
        top_k: int = 10,
    ) -> SelectedFeatureSet:
        """
        Select the top-k highest-scoring features.
        """
        validate_top_k(
            feature_count=feature_vector.dimension,
            top_k=top_k,
        )

        scores = variance_scores(
            feature_vector,
        )

        (
            indices,
            names,
            selected_scores,
        ) = select_top_features(
            feature_vector=feature_vector,
            scores=scores,
            top_k=top_k,
        )

        return SelectedFeatureSet(
            selected_indices=indices,
            selected_names=names,
            feature_scores=selected_scores,
            selection_method="variance_baseline",
        )
