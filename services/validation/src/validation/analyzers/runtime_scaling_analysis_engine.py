"""
RNAOS runtime scaling analysis engine.
"""

from __future__ import annotations

from validation.models.runtime_scaling_analysis import (
    RuntimeScalingAnalysis,
)


class RuntimeScalingAnalysisEngine:
    """
    Analyzes runtime scaling behavior.
    """

    def analyze(
        self,
        runtimes: tuple[float, ...],
    ) -> RuntimeScalingAnalysis:
        """
        Calculate runtime statistics.
        """

        if not runtimes:
            raise ValueError("No runtime values provided")

        average_runtime = sum(runtimes) / len(runtimes)

        minimum_runtime = min(runtimes)

        scaling_factor = max(runtimes) / minimum_runtime if minimum_runtime > 0 else 0.0

        return RuntimeScalingAnalysis(
            analysis_id="RUNTIME_SCALING_001",
            sample_count=len(runtimes),
            average_runtime=average_runtime,
            minimum_runtime=minimum_runtime,
            maximum_runtime=max(runtimes),
            scaling_factor=scaling_factor,
            benchmark_version="1.0.0",
        )
