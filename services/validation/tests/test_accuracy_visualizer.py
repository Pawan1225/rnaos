from pathlib import Path

from validation.visualization.accuracy_visualizer import (
    AccuracyVisualizer,
)


def test_accuracy_visualization(
    tmp_path: Path,
):

    results = [
        {
            "sequence_length": 20,
            "accuracy": 0.95,
        },
        {
            "sequence_length": 40,
            "accuracy": 0.90,
        },
    ]

    output = tmp_path / "accuracy.png"

    visualizer = AccuracyVisualizer()

    path = visualizer.generate(
        results,
        str(output),
    )

    assert path.exists()
