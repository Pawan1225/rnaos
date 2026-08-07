"""
Tests for ViennaRNA adapter.
"""

from __future__ import annotations

from dl.benchmark.adapters.vienna_adapter import (
    ViennaRNAAdapter,
)
from dl.models.benchmark.adapter_result import (
    BenchmarkAdapterResult,
)


def test_vienna_adapter() -> None:
    """
    ViennaRNA adapter produces result.
    """

    adapter = ViennaRNAAdapter()

    result = adapter.run(
        "AUGCUA",
    )

    assert isinstance(
        result,
        BenchmarkAdapterResult,
    )

    assert result.method_name == ("vienna_rna")

    assert result.sequence == ("AUGCUA")

    assert result.energy < 0
