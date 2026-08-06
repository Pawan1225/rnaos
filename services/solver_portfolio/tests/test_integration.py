from ai_intelligence.profilers.ai_profiler import (
    AIProfiler,
)
from folding.profilers.folding_profiler import (
    FoldingProfiler,
)
from optimization.profilers.optimization_profiler import (
    OptimizationProfiler,
)
from rna_intelligence.profilers.rna_profiler import (
    RNAProfiler,
)
from solver_portfolio.orchestrators.solver_orchestrator import (
    SolverOrchestrator,
)


def test_complete_pipeline():
    sequence = "GGGAAAUCC"

    rna_profile = RNAProfiler().profile(sequence)

    ai_profile = AIProfiler().profile(
        rna_profile,
    )

    folding_profile = FoldingProfiler().profile(
        sequence,
    )

    optimization = OptimizationProfiler().profile(
        ai_profile=ai_profile,
        folding_profile=folding_profile,
    )

    result = SolverOrchestrator().solve(
        optimization,
    )

    assert result.success

    assert len(result.solution) == len(sequence)
