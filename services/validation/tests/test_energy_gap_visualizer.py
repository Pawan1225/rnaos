from pathlib import Path

from validation.visualization.energy_gap_visualizer import (
    EnergyGapVisualizer,
)


def test_energy_gap_visualization(
    tmp_path: Path,
):

    results = [
        {
            "energy_gap": 0.2,
        },
        {
            "energy_gap": 0.4,
        },
        {
            "energy_gap": 0.3,
        },
    ]

    output = tmp_path / "energy_gap.png"

    visualizer = EnergyGapVisualizer()

    path = visualizer.generate(
        results,
        str(output),
    )

    assert path.exists()
