from folding.profilers.folding_profiler import FoldingProfiler
from optimization.objectives.objective_generator import (
    ObjectiveFunctionGenerator,
)


def test_objective_generation():
    folding = FoldingProfiler().profile("GGGAAAUCC")

    objective = ObjectiveFunctionGenerator().generate(folding)

    assert "ΔG" in objective.expression

    assert "MFE" in objective.expression
