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


def test_solver_orchestrator():
    sequence = "GGGAAAUCC"

    rna = RNAProfiler().profile(
        sequence,
    )

    ai = AIProfiler().profile(
        rna,
    )

    folding = FoldingProfiler().profile(
        sequence,
    )

    optimization = OptimizationProfiler().profile(
        ai_profile=ai,
        folding_profile=folding,
    )

    result = SolverOrchestrator().solve(
        optimization,
    )

    assert result.success


def test_fallback_solver():
    sequence = "GGGAAAUCC"

    rna = RNAProfiler().profile(
        sequence,
    )

    ai = AIProfiler().profile(
        rna,
    )

    folding = FoldingProfiler().profile(
        sequence,
    )

    optimization = OptimizationProfiler().profile(
        ai_profile=ai,
        folding_profile=folding,
    )

    result = SolverOrchestrator().solve(
        optimization,
        preferred_solver="does_not_exist",
    )

    assert result.success
