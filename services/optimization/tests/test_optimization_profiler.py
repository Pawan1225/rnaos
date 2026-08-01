from ai_intelligence.profilers.ai_profiler import AIProfiler
from optimization.profilers.optimization_profiler import (
    OptimizationProfiler,
)
from rna_intelligence.profilers.rna_profiler import RNAProfiler


def test_complete_optimization_pipeline():
    """Test the end-to-end optimization pipeline."""

    rna_profile = RNAProfiler().profile("GGGAAAUCC")

    ai_profile = AIProfiler().profile(rna_profile)

    optimization = OptimizationProfiler().profile(ai_profile)

    assert optimization.problem.variable_count == 9

    assert optimization.problem.constraint_count >= 2

    assert optimization.qubo.size == 9
