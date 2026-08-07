"""
RNAOS publication figure exporter.

Generates all benchmark figures
for publication package.
"""

from __future__ import annotations

import json
from pathlib import Path

from validation.visualization.accuracy_visualizer import (
    AccuracyVisualizer,
)
from validation.visualization.energy_gap_visualizer import (
    EnergyGapVisualizer,
)
from validation.visualization.quantum_resource_visualizer import (
    QuantumResourceVisualizer,
)
from validation.visualization.runtime_scaling_visualizer import (
    RuntimeScalingVisualizer,
)


class PublicationFigureExporter:
    """
    Generates publication figures.
    """

    def __init__(
        self,
        output_dir: str,
    ) -> None:

        self.output_dir = Path(output_dir)

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def export(
        self,
        results: list[dict],
    ) -> Path:
        """
        Generate publication figures.
        """

        AccuracyVisualizer().generate(
            results,
            str(self.output_dir / "accuracy_vs_length.png"),
        )

        EnergyGapVisualizer().generate(
            results,
            str(self.output_dir / "energy_gap_distribution.png"),
        )

        RuntimeScalingVisualizer().generate(
            results,
            str(self.output_dir / "runtime_scaling.png"),
        )

        QuantumResourceVisualizer().generate(
            results,
            str(self.output_dir / "quantum_resource_scaling.png"),
        )

        manifest = {
            "version": "RNAOS_v1.0",
            "figures": [
                {
                    "name": "accuracy_vs_length.png",
                    "source": "400 benchmark experiments",
                },
                {
                    "name": "energy_gap_distribution.png",
                    "source": "RNAOS energy comparison",
                },
                {
                    "name": "runtime_scaling.png",
                    "source": "benchmark runtime data",
                },
                {
                    "name": "quantum_resource_scaling.png",
                    "source": "quantum resource estimation",
                },
            ],
        }

        manifest_path = self.output_dir / "figure_manifest.json"

        manifest_path.write_text(
            json.dumps(
                manifest,
                indent=2,
            )
        )

        return manifest_path
