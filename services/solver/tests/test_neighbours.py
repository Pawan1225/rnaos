from solver.utils import NeighbourGenerator


def test_flip_one_bit() -> None:
    """Exactly one bit should change."""

    solution = [
        1,
        0,
        1,
        0,
        1,
    ]

    neighbour = NeighbourGenerator.flip_random_bit(solution)

    differences = sum(
        original != new
        for original, new in zip(
            solution,
            neighbour,
            strict=True,
        )
    )

    assert differences == 1


def test_original_solution_unchanged() -> None:
    """Original solution should not be modified."""

    solution = [
        1,
        1,
        0,
        0,
    ]

    original = solution.copy()

    _ = NeighbourGenerator.flip_random_bit(solution)

    assert solution == original


def test_neighbour_length() -> None:
    """Neighbour should preserve solution length."""

    solution = [1] * 100

    neighbour = NeighbourGenerator.flip_random_bit(solution)

    assert len(neighbour) == len(solution)


def test_neighbour_binary() -> None:
    """Neighbour should remain binary."""

    solution = [0] * 50

    neighbour = NeighbourGenerator.flip_random_bit(solution)

    assert all(value in (0, 1) for value in neighbour)
