"""
RNAOS visualization artifact generator.
"""

from __future__ import annotations

from dl.models.submission.visualization_manifest import (
    VisualizationManifest,
)


class VisualizationArtifactGenerator:
    """
    Generates visualization manifests.
    """

    def generate(
        self,
    ) -> VisualizationManifest:
        """
        Create visualization package definition.
        """

        return VisualizationManifest(
            visualization_id="VIZ_001",
            figures=(
                "architecture_diagram",
                "accuracy_comparison",
                "runtime_scaling",
                "energy_analysis",
                "solver_comparison",
            ),
            formats=(
                "PNG",
                "SVG",
                "PDF",
            ),
            generator=("VisualizationArtifactGenerator"),
            version="1.0.0",
            metadata=("release=RNAOS_v1",),
        )
