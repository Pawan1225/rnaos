import pytest
from ai_intelligence.profilers.ai_profiler import AIProfiler
from folding.profilers.folding_profiler import (
    FoldingProfiler,
)
from optimization.profilers.optimization_profiler import (
    OptimizationProfiler,
)
from rna_intelligence.profilers.rna_profiler import (
    RNAProfiler,
)


def test_short_sequence():
    """
    Very short RNA sequences cannot produce a valid
    RNA folding optimization problem because there
    are no biologically valid candidate base pairs.
    """

    sequence = "AU"

    rna_profile = RNAProfiler().profile(sequence)

    ai_profile = AIProfiler().profile(rna_profile)

    folding = FoldingProfiler().profile(sequence)

    # No candidate base pairs should exist.
    assert folding.search_space.variable_count == 0

    # Therefore no optimization problem can be built.
    with pytest.raises(ValueError):
        OptimizationProfiler().profile(
            ai_profile,
            folding,
        )


def test_long_sequence():
    """
    Moderately large RNA sequences should be supported.
    """

    # Keep unit tests reasonably fast.
    sequence = "AUGC" * 50  # 200 nucleotides

    rna_profile = RNAProfiler().profile(sequence)

    ai_profile = AIProfiler().profile(rna_profile)

    folding = FoldingProfiler().profile(sequence)

    optimization = OptimizationProfiler().profile(
        ai_profile,
        folding,
    )

    assert optimization.problem.variable_count == folding.search_space.variable_count

    assert optimization.qubo.size == folding.search_space.variable_count


def test_invalid_sequence():
    """
    Invalid RNA sequences should raise an exception.
    """

    with pytest.raises(ValueError):
        RNAProfiler().profile("XXXX")
