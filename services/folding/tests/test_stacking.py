from folding.basepairs.basepair_generator import BasePairCandidate
from folding.thermodynamics import StackingEnergyModel


def test_adjacent_stack() -> None:
    first = BasePairCandidate(
        left=0,
        right=9,
        left_base="G",
        right_base="C",
    )

    second = BasePairCandidate(
        left=1,
        right=8,
        left_base="C",
        right_base="G",
    )

    estimate = StackingEnergyModel().estimate(
        first,
        second,
    )

    assert estimate.energy == -0.5
    assert estimate.adjacent is True
    assert estimate.interaction_type == "adjacent"


def test_near_stack() -> None:
    first = BasePairCandidate(
        left=0,
        right=10,
        left_base="G",
        right_base="C",
    )

    second = BasePairCandidate(
        left=2,
        right=9,
        left_base="C",
        right_base="G",
    )

    estimate = StackingEnergyModel().estimate(
        first,
        second,
    )

    assert estimate.energy == -0.2
    assert estimate.interaction_type == "near"


def test_non_adjacent() -> None:
    first = BasePairCandidate(
        left=0,
        right=9,
        left_base="G",
        right_base="C",
    )

    second = BasePairCandidate(
        left=5,
        right=15,
        left_base="A",
        right_base="U",
    )

    estimate = StackingEnergyModel().estimate(
        first,
        second,
    )

    assert estimate.energy == 0.0
    assert estimate.interaction_type == "none"


def test_stacking_energy_wrapper() -> None:
    first = BasePairCandidate(
        left=0,
        right=9,
        left_base="G",
        right_base="C",
    )

    second = BasePairCandidate(
        left=1,
        right=8,
        left_base="C",
        right_base="G",
    )

    model = StackingEnergyModel()

    assert model.stacking_energy(first, second) == -0.5
