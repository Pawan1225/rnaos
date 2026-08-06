"""
RNAOS compute intelligence engine.
"""

from __future__ import annotations

from dl.models.compute_profile import (
    ComputeProfile,
)


class ComputeIntelligenceEngine:
    """
    Recommends compute resources.
    """

    def analyze(
        self,
        model_size: str,
        sequence_length: int,
    ) -> ComputeProfile:
        """
        Generate compute recommendation.
        """

        if model_size == "large":
            return ComputeProfile(
                backend="gpu",
                device_count=1,
                estimated_memory_gb=16.0,
            )

        if sequence_length > 1000:
            return ComputeProfile(
                backend="hpc",
                device_count=4,
                estimated_memory_gb=64.0,
            )

        return ComputeProfile(
            backend="cpu",
            device_count=1,
            estimated_memory_gb=4.0,
        )
