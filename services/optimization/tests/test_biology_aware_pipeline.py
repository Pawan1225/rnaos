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


def test_complete_biology_pipeline():
    """Test the complete biology-aware optimization pipeline."""

    sequence = "GGGAAAUCC"

    #
    # RNA Intelligence
    #

    rna = RNAProfiler().profile(
        sequence,
    )

    #
    # AI Intelligence
    #

    ai = AIProfiler().profile(
        rna,
    )

    #
    # Folding Intelligence
    #

    folding = FoldingProfiler().profile(
        sequence,
    )

    #
    # Optimization
    #

    optimization = OptimizationProfiler().profile(
        ai,
        folding,
    )

    #
    # Variables
    #

    assert optimization.problem.variable_count == folding.search_space.variable_count

    #
    # Constraints
    #

    assert optimization.problem.constraint_count == folding.search_space.conflict_count

    #
    # Metadata
    #

    assert optimization.problem.metadata.candidate_pair_count == folding.search_space.variable_count

    assert optimization.problem.metadata.conflict_count == folding.search_space.conflict_count

    #
    # QUBO
    #

    assert optimization.qubo.size == folding.search_space.variable_count
