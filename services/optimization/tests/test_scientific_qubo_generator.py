from folding.profilers.folding_profiler import FoldingProfiler
from optimization.generators.scientific_qubo_generator import (
    ScientificQUBOGenerator,
)


def test_qubo_size() -> None:
    folding = FoldingProfiler().profile(
        "GGGAAAUCC",
    )

    variables = [f"x_{c.left}_{c.right}" for c in folding.search_space.candidates]

    qubo = ScientificQUBOGenerator().generate(
        folding,
        variables,
    )

    assert qubo.size == len(variables)


def test_qubo_symmetry() -> None:
    folding = FoldingProfiler().profile(
        "GGGAAAUCC",
    )

    variables = [f"x_{c.left}_{c.right}" for c in folding.search_space.candidates]

    qubo = ScientificQUBOGenerator().generate(
        folding,
        variables,
    )

    for i in range(qubo.size):
        for j in range(qubo.size):
            assert qubo.matrix[i][j] == qubo.matrix[j][i]


def test_diagonal_contains_energy() -> None:
    folding = FoldingProfiler().profile(
        "GGGAAAUCC",
    )

    variables = [f"x_{c.left}_{c.right}" for c in folding.search_space.candidates]

    qubo = ScientificQUBOGenerator().generate(
        folding,
        variables,
    )

    assert any(qubo.matrix[i][i] != 0.0 for i in range(qubo.size))


def test_conflict_penalty_positive() -> None:
    generator = ScientificQUBOGenerator()

    assert generator.conflict_penalty > 0
