import pytest
from folding.thermodynamics import EnergyParameters


@pytest.mark.parametrize(
    ("pair", "expected"),
    [
        ("AU", -2.0),
        ("UA", -2.0),
        ("GC", -3.0),
        ("CG", -3.0),
        ("GU", -1.0),
        ("UG", -1.0),
    ],
)
def test_base_pair_energies(pair: str, expected: float) -> None:
    assert EnergyParameters.base_pair_energy(pair) == expected


@pytest.mark.parametrize(
    "pair",
    [
        "au",
        "gc",
        "Gu",
        "uG",
    ],
)
def test_case_insensitive_lookup(pair: str) -> None:
    """
    Base-pair lookup should be case-insensitive.
    """
    assert EnergyParameters.base_pair_energy(pair) == EnergyParameters.metadata(pair).energy


@pytest.mark.parametrize(
    "pair",
    [
        "AA",
        "TT",
        "GG",
        "CC",
        "AC",
        "CA",
        "",
        "A",
        "XYZ",
    ],
)
def test_invalid_base_pair(pair: str) -> None:
    with pytest.raises(ValueError):
        EnergyParameters.base_pair_energy(pair)


def test_energy_ordering() -> None:
    """
    GC should be more stable than AU,
    which should be more stable than GU.
    """
    assert (
        EnergyParameters.base_pair_energy("GC")
        < EnergyParameters.base_pair_energy("AU")
        < EnergyParameters.base_pair_energy("GU")
    )


def test_number_of_supported_pairs() -> None:
    assert len(EnergyParameters.BASE_PAIR_ENERGIES) == 6


def test_hydrogen_bonds_gc() -> None:
    assert EnergyParameters.hydrogen_bonds("GC") == 3


def test_hydrogen_bonds_au() -> None:
    assert EnergyParameters.hydrogen_bonds("AU") == 2


def test_supported_pairs() -> None:
    assert EnergyParameters.supported_pairs() == (
        "AU",
        "CG",
        "GC",
        "GU",
        "UA",
        "UG",
    )


def test_metadata_object() -> None:
    metadata = EnergyParameters.metadata("GC")

    assert metadata.pair == "GC"
    assert metadata.energy == -3.0
    assert metadata.hydrogen_bonds == 3


def test_supported_pair_validation() -> None:
    assert EnergyParameters.is_supported_pair("GC")
    assert EnergyParameters.is_supported_pair("gc")
    assert EnergyParameters.is_supported_pair("Au")
    assert not EnergyParameters.is_supported_pair("AA")
    assert not EnergyParameters.is_supported_pair("AC")
