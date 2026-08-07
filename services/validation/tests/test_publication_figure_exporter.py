from pathlib import Path

from validation.export.publication_figure_exporter import (
    PublicationFigureExporter,
)


def test_publication_figure_export():

    results = [
        {
            "sequence_length": 20,
            "accuracy": 0.95,
            "energy_gap": 0.2,
            "runtime_seconds": 0.1,
            "estimated_qubits": 40,
        },
        {
            "sequence_length": 40,
            "accuracy": 0.90,
            "energy_gap": 0.3,
            "runtime_seconds": 0.3,
            "estimated_qubits": 80,
        },
    ]

    output = Path("publication/test_figures")

    exporter = PublicationFigureExporter(str(output))

    manifest = exporter.export(results)

    assert manifest.exists()

    assert (output / "accuracy_vs_length.png").exists()

    assert (output / "figure_manifest.json").exists()
