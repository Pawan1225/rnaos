from ai_intelligence.profilers.ai_profiler import AIProfiler
from optimization.profilers.optimization_profiler import (
    OptimizationProfiler,
)
from rna_intelligence.profilers.rna_profiler import RNAProfiler


def test_end_to_end_pipeline():
    """Test the complete RNAOS optimization pipeline."""

    sequence = "GGGAAAUCC"

    rna_profile = RNAProfiler().profile(sequence)

    ai_profile = AIProfiler().profile(rna_profile)

    optimization = OptimizationProfiler().profile(ai_profile)

    assert optimization.problem.variable_count == len(sequence)

    assert optimization.qubo.size == len(sequence)

    assert optimization.problem.metadata.solver_hint == ai_profile.recommendation.solver
