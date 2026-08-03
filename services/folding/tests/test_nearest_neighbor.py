from folding.basepairs.basepair_generator import BasePairCandidate
from folding.thermodynamics import NearestNeighborModel


def test_gc_pair() -> None:
    candidate = BasePairCandidate(
        left=0,
        right=8,
        left_base="G",
        right_base="C",
    )

    estimate = NearestNeighborModel().estimate(candidate)

    assert estimate.pair == "GC"
    assert estimate.energy == -3.0
    assert estimate.hydrogen_bonds == 3


def test_au_pair() -> None:
    candidate = BasePairCandidate(
        left=0,
        right=5,
        left_base="A",
        right_base="U",
    )

    estimate = NearestNeighborModel().estimate(candidate)

    assert estimate.energy == -2.0
    assert estimate.hydrogen_bonds == 2


def test_gu_pair() -> None:
    candidate = BasePairCandidate(
        left=2,
        right=7,
        left_base="G",
        right_base="U",
    )

    estimate = NearestNeighborModel().estimate(candidate)

    assert estimate.energy == -1.0
    assert estimate.hydrogen_bonds == 2


def test_pair_energy_wrapper() -> None:
    candidate = BasePairCandidate(
        left=0,
        right=8,
        left_base="G",
        right_base="C",
    )

    model = NearestNeighborModel()

    assert model.pair_energy(candidate) == -3.0
