"""
Tests for compute intelligence engine.
"""

from __future__ import annotations

from dl.engines.compute_intelligence_engine import (
    ComputeIntelligenceEngine,
)
from dl.models.compute_profile import (
    ComputeProfile,
)


def test_large_model_uses_gpu() -> None:
    """
    Large models require GPU.
    """

    engine = ComputeIntelligenceEngine()

    profile = engine.analyze(
        model_size="large",
        sequence_length=500,
    )

    assert isinstance(
        profile,
        ComputeProfile,
    )

    assert profile.backend == "gpu"

    assert profile.device_count == 1


def test_long_sequence_uses_hpc() -> None:
    """
    Long RNA sequences use HPC.
    """

    engine = ComputeIntelligenceEngine()

    profile = engine.analyze(
        model_size="medium",
        sequence_length=2000,
    )

    assert profile.backend == "hpc"

    assert profile.device_count == 4


def test_default_cpu_execution() -> None:
    """
    Small workloads use CPU.
    """

    engine = ComputeIntelligenceEngine()

    profile = engine.analyze(
        model_size="small",
        sequence_length=100,
    )

    assert profile.backend == "cpu"
