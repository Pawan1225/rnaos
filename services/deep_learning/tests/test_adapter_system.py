"""
Tests for benchmark adapter system.
"""

from __future__ import annotations

from dl.benchmark.adapters.rnaos_adapter import (
    RNAOSAdapter,
)
from dl.benchmark.adapters.vienna_adapter import (
    ViennaRNAAdapter,
)
from dl.models.benchmark.adapter_result import (
    BenchmarkAdapterResult,
)


def test_adapter_names() -> None:
    """
    Adapters expose unique names.
    """

    vienna = ViennaRNAAdapter()

    rnaos = RNAOSAdapter()

    assert vienna.name == ("vienna_rna")

    assert rnaos.name == ("rnaos_hybrid")


def test_adapter_result_consistency() -> None:
    """
    Different adapters return same result format.
    """

    sequence = "AUGCUA"

    vienna_result = ViennaRNAAdapter().run(
        sequence,
    )

    rnaos_result = RNAOSAdapter().run(
        sequence,
    )

    assert isinstance(
        vienna_result,
        BenchmarkAdapterResult,
    )

    assert isinstance(
        rnaos_result,
        BenchmarkAdapterResult,
    )

    assert vienna_result.sequence == (sequence)

    assert rnaos_result.sequence == (sequence)

    assert vienna_result.method_name == ("vienna_rna")

    assert rnaos_result.method_name == ("rnaos_hybrid")

    assert vienna_result.energy < 0

    assert rnaos_result.energy < 0


def test_adapter_metadata() -> None:
    """
    Adapter outputs preserve provenance.
    """

    vienna_result = ViennaRNAAdapter().run(
        "AUGCUA",
    )

    rnaos_result = RNAOSAdapter().run(
        "AUGCUA",
    )

    assert (
        len(
            vienna_result.metadata,
        )
        > 0
    )

    assert (
        len(
            rnaos_result.metadata,
        )
        > 0
    )
