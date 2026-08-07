from pathlib import Path

from validation.visualization.runtime_scaling_visualizer import (
    RuntimeScalingVisualizer,
)


def test_runtime_scaling_visualization(
    tmp_path: Path,
):

    results = [
        {
            "sequence_length": 20,
            "runtime_seconds": 0.1,
        },
        {
            "sequence_length": 40,
            "runtime_seconds": 0.3,
        },
        {
            "sequence_length": 80,
            "runtime_seconds": 1.0,
        },
    ]

    output = tmp_path / "runtime_scaling.png"

    visualizer = RuntimeScalingVisualizer()

    path = visualizer.generate(
        results,
        str(output),
    )

    assert path.exists()
