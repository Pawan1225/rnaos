from ai_intelligence.profilers.ai_profiler import AIProfiler
from folding.profilers.folding_profiler import (
    FoldingProfiler,
)
from optimization.profilers.optimization_profiler import (
    OptimizationProfiler,
)
from rna_intelligence.profilers.rna_profiler import RNAProfiler


def test_end_to_end_pipeline():
    """Test the complete RNAOS optimization pipeline."""

    sequence = "GGGAAAUCC"

    # RNA Intelligence
    rna_profile = RNAProfiler().profile(sequence)

    # AI Intelligence
    ai_profile = AIProfiler().profile(rna_profile)

    # RNA Folding Intelligence
    folding = FoldingProfiler().profile(sequence)

    # Optimization
    optimization = OptimizationProfiler().profile(
        ai_profile,
        folding,
    )

    # ------------------------------------------------------------------
    # Optimization variables
    # ------------------------------------------------------------------
    assert optimization.problem.variable_count == folding.search_space.variable_count

    # ------------------------------------------------------------------
    # QUBO
    # ------------------------------------------------------------------
    assert optimization.qubo.size == folding.search_space.variable_count

    # ------------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------------
    assert optimization.problem.metadata.solver_hint == ai_profile.recommendation.solver

    assert optimization.problem.metadata.candidate_pair_count == folding.search_space.variable_count

    assert optimization.problem.metadata.conflict_count == folding.search_space.conflict_count

    assert isinstance(
        optimization.problem.metadata.mfe,
        float,
    )

    assert isinstance(
        optimization.problem.metadata.energy_gap,
        float,
    )

    # ------------------------------------------------------------------
    # Objective & Constraints
    # ------------------------------------------------------------------
    assert optimization.problem.objective is not None

    assert optimization.problem.constraint_count == len(optimization.problem.constraints)

    # ------------------------------------------------------------------
    # QUBO Matrix
    # ------------------------------------------------------------------
    assert len(optimization.qubo.matrix) == optimization.qubo.size

    assert len(optimization.qubo.matrix[0]) == optimization.qubo.size
