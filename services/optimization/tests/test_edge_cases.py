import pytest
from ai_intelligence.profilers.ai_profiler import AIProfiler
from optimization.profilers.optimization_profiler import (
    OptimizationProfiler,
)
from rna_intelligence.profilers.rna_profiler import RNAProfiler


def test_short_sequence():
    """Very small RNA sequences should be supported."""

    profile = RNAProfiler().profile("AU")

    ai = AIProfiler().profile(profile)

    optimization = OptimizationProfiler().profile(ai)

    assert optimization.problem.variable_count == 2


def test_long_sequence():
    """Large RNA sequences should also be supported."""

    sequence = "AUGC" * 250

    profile = RNAProfiler().profile(sequence)

    ai = AIProfiler().profile(profile)

    optimization = OptimizationProfiler().profile(ai)

    assert optimization.problem.variable_count == len(sequence)


def test_invalid_sequence():
    """Invalid RNA sequences should raise an exception."""

    with pytest.raises(ValueError):
        RNAProfiler().profile("XXXX")
