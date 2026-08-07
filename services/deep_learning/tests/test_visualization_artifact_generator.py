"""
Tests for visualization artifact generator.
"""

from __future__ import annotations

from dl.submission.visualization.visualization_artifact_generator import (
    VisualizationArtifactGenerator,
)


def test_visualization_artifact_generation() -> None:
    """
    Visualization artifact manifest is generated.
    """

    generator = VisualizationArtifactGenerator()

    manifest = generator.generate()

    assert manifest.visualization_id == ("VIZ_001")

    assert "runtime_scaling" in manifest.figures

    assert "PDF" in manifest.formats

    assert manifest.version == ("1.0.0")
