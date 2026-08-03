from folding.profilers.folding_profiler import (
    FoldingProfiler,
)
from optimization.generators.qubo_generator import (
    QUBOGenerator,
)


def test_qubo_generation():
    """Test generation of an RNA Folding QUBO."""

    folding = FoldingProfiler().profile("GGGAAAUCC")

    variable_names = [
        f"x_{candidate.left}_{candidate.right}" for candidate in folding.search_space.candidates
    ]

    qubo = QUBOGenerator().generate(
        folding,
        variable_names,
    )

    assert qubo.size == len(variable_names)

    assert qubo.variable_names == variable_names

    assert len(qubo.matrix) == qubo.size

    assert len(qubo.matrix[0]) == qubo.size


def test_diagonal_negative():
    """All diagonal entries should reward selecting a base pair."""

    folding = FoldingProfiler().profile("GGGAAAUCC")

    variable_names = [
        f"x_{candidate.left}_{candidate.right}" for candidate in folding.search_space.candidates
    ]

    qubo = QUBOGenerator().generate(
        folding,
        variable_names,
    )

    for i in range(qubo.size):
        assert qubo.matrix[i][i] == -1.0


def test_conflict_penalties():
    """Conflict edges should produce positive QUBO penalties."""

    folding = FoldingProfiler().profile("GGGAAAUCC")

    variable_names = [
        f"x_{candidate.left}_{candidate.right}" for candidate in folding.search_space.candidates
    ]

    qubo = QUBOGenerator().generate(
        folding,
        variable_names,
    )

    for edge in folding.search_space.conflicts:
        assert qubo.matrix[edge.first][edge.second] > 0.0
        assert qubo.matrix[edge.second][edge.first] > 0.0
