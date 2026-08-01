from ai_intelligence.profilers.ai_profiler import AIProfiler
from optimization.constraints.constraint_generator import (
    ConstraintGenerator,
)
from rna_intelligence.profilers.rna_profiler import RNAProfiler


def test_generate_constraints():
    """Test constraint generation from an AI profile."""

    rna_profile = RNAProfiler().profile("GGGAAAUCC")

    ai_profile = AIProfiler().profile(rna_profile)

    constraints = ConstraintGenerator().generate(ai_profile)

    assert len(constraints) >= 2

    assert constraints[0].name == "binary_variables"

    assert constraints[1].name == "sequence_length"
