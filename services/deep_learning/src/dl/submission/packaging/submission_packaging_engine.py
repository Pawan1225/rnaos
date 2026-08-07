"""
RNAOS submission packaging engine.
"""

from __future__ import annotations

from dl.models.submission.submission_manifest import (
    SubmissionManifest,
)


class SubmissionPackagingEngine:
    """
    Builds submission package definitions.
    """

    def build(
        self,
    ) -> SubmissionManifest:
        """
        Create submission package manifest.
        """

        return SubmissionManifest(
            submission_id="SUBMISSION_001",
            version="1.0.0",
            artifacts=(
                "documentation",
                "scientific_report",
                "benchmark_report",
                "figures",
                "presentation",
                "reproducibility",
            ),
            directories=(
                "docs",
                "reports",
                "figures",
                "presentation",
                "reproducibility",
                "code",
            ),
            package_name=("RNAOS_v1.0.0_Submission"),
            metadata=("release=RNAOS_v1",),
        )
