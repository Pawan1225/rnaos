"""
Tests for visualization dataset.
"""

from validation.models.visualization_dataset import (
    VisualizationDataset,
)


def test_visualization_dataset():

    dataset = VisualizationDataset(
        dataset_id="VISUALIZATION_001",
        benchmark_version="1.0.0",
        sequence_lengths=(
            20,
            20,
            40,
        ),
        accuracy_values=(
            0.95,
            0.94,
            0.90,
        ),
        energy_gaps=(
            0.2,
            0.3,
            0.5,
        ),
        runtime_values=(
            1.0,
            1.2,
            2.0,
        ),
        qubit_estimates=(
            20,
            20,
            40,
        ),
        solvers=("hybrid_quantum_inspired",),
        metadata=("publication_ready",),
    )

    assert dataset.dataset_id == ("VISUALIZATION_001")

    assert len(dataset.accuracy_values) == 3

    assert dataset.benchmark_version == ("1.0.0")
