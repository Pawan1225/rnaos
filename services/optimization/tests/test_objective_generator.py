from ai_intelligence.profilers.ai_profiler import AIProfiler
from optimization.objectives.objective_generator import (
    ObjectiveFunctionGenerator,
)
from rna_intelligence.profilers.rna_profiler import RNAProfiler


def test_generate_objective():
    """Test objective generation from an AI profile."""

    rna_profile = RNAProfiler().profile("GGGAAAUCC")

    ai_profile = AIProfiler().profile(rna_profile)

    objective = ObjectiveFunctionGenerator().generate(ai_profile)

    assert objective.sense == "minimize"
    assert "complexity" in objective.expression
