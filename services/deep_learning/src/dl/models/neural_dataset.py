"""
RNAOS neural dataset model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class NeuralDataset:
    """
    Immutable deep learning dataset.

    Stores tensor-ready biological inputs
    used by neural architectures.
    """

    sequence_tensors: tuple[tuple[float, ...], ...]

    structure_tensors: tuple[tuple[float, ...], ...]

    thermodynamic_features: tuple[float, ...]

    targets: tuple[float, ...]

    dataset_version: str

    sample_count: int

    @property
    def feature_count(
        self,
    ) -> int:
        """
        Number of thermodynamic features.
        """

        return len(
            self.thermodynamic_features,
        )

    @property
    def sequence_length(
        self,
    ) -> int:
        """
        Length of encoded RNA sequence.
        """

        if not self.sequence_tensors:
            return 0

        return len(
            self.sequence_tensors[0],
        )
