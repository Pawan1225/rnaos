from folding.profilers.folding_profiler import (
    FoldingProfiler,
)
from optimization.constraints.constraint_generator import (
    ConstraintGenerator,
)


def test_generate_constraints():
    """Test biological constraint generation."""

    folding = FoldingProfiler().profile("GGGAAAUCC")

    constraints = ConstraintGenerator().generate(
        folding,
    )

    assert isinstance(
        constraints,
        list,
    )

    assert len(constraints) == folding.search_space.conflict_count


def test_constraint_format():
    """Every conflict becomes a binary incompatibility constraint."""

    folding = FoldingProfiler().profile("GGGAAAUCC")

    constraints = ConstraintGenerator().generate(
        folding,
    )

    for constraint in constraints:
        assert constraint.name.startswith("conflict_")

        assert "<= 1" in constraint.expression

        assert "x_" in constraint.expression
