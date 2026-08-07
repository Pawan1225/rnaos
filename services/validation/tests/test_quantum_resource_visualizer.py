from pathlib import Path

from validation.visualization.quantum_resource_visualizer import (
    QuantumResourceVisualizer,
)


def test_quantum_resource_visualization(
    tmp_path: Path,
):

    results = [
        {
            "sequence_length": 20,
            "estimated_qubits": 40,
        },
        {
            "sequence_length": 40,
            "estimated_qubits": 80,
        },
        {
            "sequence_length": 80,
            "estimated_qubits": 160,
        },
    ]

    output = tmp_path / "quantum_scaling.png"

    visualizer = QuantumResourceVisualizer()

    path = visualizer.generate(
        results,
        str(output),
    )

    assert path.exists()
