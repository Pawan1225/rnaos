from ai_intelligence.profilers.ai_profiler import (
    AIProfiler,
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

    rna = RNAProfiler().profile(sequence)

    ai = AIProfiler().profile(rna)

    optimization = OptimizationProfiler().profile(ai)

    orchestrator = SolverOrchestrator()

    result = orchestrator.solve(optimization)

    assert result.success

    assert len(result.solution) == len(sequence)


def test_fallback_solver():
    sequence = "GGGAAAUCC"

    rna = RNAProfiler().profile(sequence)

    ai = AIProfiler().profile(rna)

    optimization = OptimizationProfiler().profile(ai)

    optimization.problem.metadata.solver_hint = "unknown"

    result = SolverOrchestrator().solve(
        optimization,
    )

    assert result.solver_name == "greedy"
