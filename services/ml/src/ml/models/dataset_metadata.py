"""
RNAOS machine learning dataset metadata.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class DatasetMetadata:
    """
    Immutable metadata describing an ML dataset.

    Stores dataset lineage, schema information,
    and dataset statistics required for
    reproducible machine learning experiments.
    """

    dataset_id: str

    version: str

    feature_count: int

    sample_count: int

    source: str

    schema_version: str

    created_at: str

    @property
    def size(
        self,
    ) -> int:
        """
        Total dataset dimensions.

        Returns:
            Number of feature values.
        """

        return self.feature_count * self.sample_count

    @property
    def is_valid(
        self,
    ) -> bool:
        """
        Validate dataset metadata.
        """

        return self.feature_count > 0 and self.sample_count > 0
