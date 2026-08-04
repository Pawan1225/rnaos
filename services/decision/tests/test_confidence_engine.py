from decision.confidence.confidence_engine import (
    ConfidenceEngine,
)


def test_high_confidence():
    """Small deterministic problems should produce high confidence."""

    score = ConfidenceEngine().score(
        problem_size=20,
        relative_error=0.02,
        deterministic_solver=True,
    )

    assert score > 0.90


def test_large_problem():
    """Large optimization problems should reduce confidence."""

    score = ConfidenceEngine().score(
        problem_size=600,
        relative_error=0.20,
        deterministic_solver=False,
    )

    assert score < 0.80


def test_bounds():
    """Confidence must remain within [0.0, 1.0]."""

    score = ConfidenceEngine().score(
        problem_size=10_000,
        relative_error=5.0,
        deterministic_solver=False,
    )

    assert 0.0 <= score <= 1.0


def test_deterministic_bonus():
    """Deterministic solvers should increase confidence."""

    engine = ConfidenceEngine()

    deterministic = engine.score(
        problem_size=50,
        relative_error=0.05,
        deterministic_solver=True,
    )

    nondeterministic = engine.score(
        problem_size=50,
        relative_error=0.05,
        deterministic_solver=False,
    )

    assert deterministic > nondeterministic
