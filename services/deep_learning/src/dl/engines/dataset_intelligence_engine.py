"""
RNAOS dataset intelligence engine.
"""

from __future__ import annotations

from dl.models.dataset_profile import (
    DatasetProfile,
)


class DatasetIntelligenceEngine:
    """
    Evaluates dataset readiness.
    """

    def analyze(
        self,
        dataset_name: str,
        sample_count: int,
        feature_dimension: int,
    ) -> DatasetProfile:
        """
        Generate dataset profile.
        """

        score = min(
            (sample_count / 1000) + (feature_dimension / 100),
            1.0,
        )

        return DatasetProfile(
            dataset_name=dataset_name,
            sample_count=sample_count,
            feature_dimension=feature_dimension,
            readiness_score=round(
                score,
                4,
            ),
        )
