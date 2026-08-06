"""
RNAOS machine learning feature metadata.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class FeatureMetadata:
    """
    Immutable metadata describing an ML feature.

    Tracks feature identity, lineage,
    and lifecycle information.
    """

    feature_name: str

    version: str

    source: str

    description: str

    created_at: str

    @property
    def identifier(
        self,
    ) -> str:
        """
        Unique feature identifier.
        """

        return f"{self.feature_name}:{self.version}"
