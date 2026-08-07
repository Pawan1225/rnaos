"""
RNAOS final submission generator.
"""

from __future__ import annotations

from dl.models.submission.final_submission_profile import (
    FinalSubmissionProfile,
)


class FinalSubmissionGenerator:
    """
    Master submission orchestrator.
    """

    def generate(
        self,
    ) -> FinalSubmissionProfile:
        """
        Generate final submission profile.
        """

        return FinalSubmissionProfile(
            submission_id="FINAL_SUBMISSION_001",
            version="1.0.0",
            components=(
                "documentation",
                "scientific_report",
                "benchmark_report",
                "visualizations",
                "presentation",
                "reproducibility",
                "submission_package",
                "release_artifacts",
            ),
            package_name=("RNAOS_v1.0.0"),
            release_ready=True,
            metadata=("WISER_Modern_submission",),
        )
