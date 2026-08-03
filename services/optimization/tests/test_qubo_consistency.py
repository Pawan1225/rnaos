from folding.profilers.folding_profiler import (
    FoldingProfiler,
)
from optimization.generators.qubo_generator import (
    QUBOGenerator,
)


def test_qubo_dimensions():
    """QUBO matrix should have consistent dimensions."""

    folding = FoldingProfiler().profile("GGGAAAUCC")

    variables = [
        f"x_{candidate.left}_{candidate.right}" for candidate in folding.search_space.candidates
    ]

    qubo = QUBOGenerator().generate(
        folding,
        variables,
    )

    assert len(qubo.matrix) == qubo.size

    for row in qubo.matrix:
        assert len(row) == qubo.size


def test_qubo_symmetry():
    """QUBO matrices must be symmetric."""

    folding = FoldingProfiler().profile("GGGAAAUCC")

    variables = [
        f"x_{candidate.left}_{candidate.right}" for candidate in folding.search_space.candidates
    ]

    qubo = QUBOGenerator().generate(
        folding,
        variables,
    )

    for i in range(qubo.size):
        for j in range(qubo.size):
            assert qubo.matrix[i][j] == qubo.matrix[j][i]
