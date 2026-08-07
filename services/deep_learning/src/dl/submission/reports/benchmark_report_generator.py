"""
RNAOS benchmark report generator.
"""

from __future__ import annotations

from dl.models.submission.benchmark_report_artifact import (
    BenchmarkReportArtifact,
)


class BenchmarkReportGenerator:
    """
    Generates benchmark report artifacts.
    """

    def generate(
        self,
    ) -> BenchmarkReportArtifact:
        """
        Create benchmark report definition.
        """

        return BenchmarkReportArtifact(
            report_id="BENCHMARK_REPORT_001",
            title=("RNAOS Scientific Benchmark Report"),
            benchmarks=(
                "ViennaRNA comparison",
                "RNAOS hybrid optimization",
                "Solver scalability",
            ),
            metrics=(
                "accuracy",
                "energy",
                "runtime",
                "precision",
                "recall",
                "F1",
            ),
            figures=(
                "accuracy_comparison.png",
                "runtime_scaling.png",
                "energy_analysis.png",
            ),
            version="1.0.0",
            metadata=("benchmark_framework=14.7",),
        )
