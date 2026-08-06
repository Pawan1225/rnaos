"""
Tests for RNAOS NeuralDataset.
"""

from __future__ import annotations

from dl.models.neural_dataset import (
    NeuralDataset,
)


def test_neural_dataset_creation() -> None:
    """
    Neural dataset can be created.
    """

    dataset = NeuralDataset(
        sequence_tensors=(
            (
                1.0,
                0.0,
            ),
        ),
        structure_tensors=(
            (
                0.5,
                0.5,
            ),
        ),
        thermodynamic_features=(
            0.8,
            0.2,
        ),
        targets=(1.0,),
        dataset_version="v1",
        sample_count=1,
    )

    assert dataset.sample_count == 1

    assert dataset.feature_count == 2

    assert dataset.sequence_length == 2
