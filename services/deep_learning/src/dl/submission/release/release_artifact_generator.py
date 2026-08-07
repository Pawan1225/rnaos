"""
RNAOS release artifact generator.
"""

from __future__ import annotations

from dl.models.submission.release_manifest import (
    ReleaseManifest,
)


class ReleaseArtifactGenerator:
    """
    Generates release manifests.
    """

    def generate(
        self,
    ) -> ReleaseManifest:
        """
        Create release definition.
        """

        return ReleaseManifest(
            release_id="RELEASE_001",
            version="1.0.0",
            package_name=("RNAOS_v1.0.0"),
            artifacts=(
                "submission_package",
                "scientific_report",
                "benchmark_report",
                "presentation",
                "reproducibility_package",
            ),
            checksum_file=("checksums.txt"),
            changelog_file=("CHANGELOG.md"),
            metadata=("release=RNAOS_v1",),
        )
