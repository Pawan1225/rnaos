"""
RNAOS selected feature set model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class SelectedFeatureSet:
    """
    Immutable feature selection result.
    """

    selected_indices: tuple[int, ...]

    selected_names: tuple[str, ...]

    feature_scores: tuple[float, ...]

    selection_method: str

    @property
    def feature_count(
        self,
    ) -> int:
        """
        Number of selected features.
        """
        return len(
            self.selected_indices,
        )

    @property
    def is_empty(
        self,
    ) -> bool:
        """
        Whether any features were selected.
        """
        return self.feature_count == 0
