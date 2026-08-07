"""
Tests for ViennaRNA reference runner.
"""

from validation.runners.vienna_reference_runner import (
    ViennaReferenceRunner,
)


def test_vienna_reference_generation() -> None:
    """
    ViennaRNA result generation works.
    """

    runner = ViennaReferenceRunner()

    result = runner.run(
        "GGGAAAUCC",
    )

    assert result.engine == ("ViennaRNA")

    assert result.length == 9

    assert isinstance(
        result.structure,
        str,
    )

    assert isinstance(
        result.mfe_energy,
        float,
    )
