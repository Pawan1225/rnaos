from ai_intelligence.profilers.ai_profiler import AIProfiler
from folding.profilers.folding_profiler import FoldingProfiler
from optimization.profilers.optimization_profiler import (
    OptimizationProfiler,
)
from rna_intelligence.profilers.rna_profiler import RNAProfiler


def test_complete_optimization_pipeline():
    """Test the end-to-end optimization pipeline."""

    sequence = "GGGAAAUCC"

    rna_profile = RNAProfiler().profile(sequence)

    ai_profile = AIProfiler().profile(rna_profile)

    folding = FoldingProfiler().profile(sequence)

    optimization = OptimizationProfiler().profile(
        ai_profile,
        folding,
    )

    # ------------------------------------------------------------------
    # Decision variables
    # ------------------------------------------------------------------
    assert optimization.problem.variable_count == folding.search_space.variable_count

    assert optimization.problem.variables[0].name.startswith("x_")

    # ------------------------------------------------------------------
    # Biology-aware metadata
    # ------------------------------------------------------------------
    assert optimization.problem.metadata.candidate_pair_count == folding.search_space.variable_count

    assert optimization.problem.metadata.conflict_count == folding.search_space.conflict_count

    assert optimization.problem.metadata.estimated_qubo_size == folding.search_space.variable_count

    assert isinstance(
        optimization.problem.metadata.mfe,
        float,
    )

    assert isinstance(
        optimization.problem.metadata.energy_gap,
        float,
    )

    assert optimization.problem.metadata.search_space_density >= 0.0

    # ------------------------------------------------------------------
    # Optimization problem
    # ------------------------------------------------------------------
    assert optimization.problem.constraint_count == len(optimization.problem.constraints)

    assert optimization.problem.objective is not None

    assert optimization.qubo is not None
