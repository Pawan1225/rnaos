from solver.utils import MetropolisAcceptanceCriterion


def test_accept_better_solution() -> None:
    """Better solutions should always be accepted."""

    assert MetropolisAcceptanceCriterion.accept(
        current_objective=10.0,
        candidate_objective=5.0,
        temperature=1.0,
    )


def test_accept_equal_solution() -> None:
    """Equal solutions should always be accepted."""

    assert MetropolisAcceptanceCriterion.accept(
        current_objective=10.0,
        candidate_objective=10.0,
        temperature=1.0,
    )


def test_reject_when_temperature_zero() -> None:
    """Worse solutions should be rejected at zero temperature."""

    assert not MetropolisAcceptanceCriterion.accept(
        current_objective=5.0,
        candidate_objective=10.0,
        temperature=0.0,
    )


def test_acceptance_returns_bool() -> None:
    """Acceptance criterion should always return a boolean."""

    result = MetropolisAcceptanceCriterion.accept(
        current_objective=10.0,
        candidate_objective=11.0,
        temperature=5.0,
    )

    assert isinstance(result, bool)
