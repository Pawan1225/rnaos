from folding.basepairs.basepair_generator import BasePairCandidate
from folding.thermodynamics import ScientificEnergyModel


def test_single_pair_energy() -> None:
    candidate = BasePairCandidate(
        left=0,
        right=8,
        left_base="G",
        right_base="C",
    )

    estimate = ScientificEnergyModel().estimate(candidate)

    assert estimate.base_pair_energy == -3.0
    assert estimate.loop_energy > 0
    assert estimate.stacking_energy == 0.0
    assert estimate.total_energy == (estimate.base_pair_energy + estimate.loop_energy)


def test_stacked_pair_energy() -> None:
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

    estimate = ScientificEnergyModel().estimate(
        second,
        previous=first,
    )

    assert estimate.stacking_energy < 0
    assert estimate.total_energy == (
        estimate.base_pair_energy + estimate.stacking_energy + estimate.loop_energy
    )
