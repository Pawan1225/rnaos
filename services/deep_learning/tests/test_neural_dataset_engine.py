"""
Tests for RNAOS Neural Dataset Engine.
"""

from __future__ import annotations

from dl.engines.neural_dataset_engine import (
    NeuralDatasetEngine,
)
from dl.models.neural_dataset import (
    NeuralDataset,
)


def test_dataset_build() -> None:
    """
    Neural dataset is created correctly.
    """

    engine = NeuralDatasetEngine()

    dataset = engine.build(
        sequence="AUGC",
        structure="().",
        thermodynamic_features=(
            -5.2,
            0.5,
        ),
        targets=(1.0,),
    )

    assert isinstance(
        dataset,
        NeuralDataset,
    )

    assert dataset.sample_count == 1

    assert dataset.sequence_length == 4

    assert dataset.feature_count == 2
