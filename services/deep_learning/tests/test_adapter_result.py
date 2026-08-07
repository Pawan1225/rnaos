"""
Tests for benchmark adapter result.
"""

from __future__ import annotations

from dl.models.benchmark.adapter_result import (
    BenchmarkAdapterResult,
)


def test_adapter_result() -> None:
    """
    Adapter result can be created.
    """

    result = BenchmarkAdapterResult(
        method_name="vienna_rna",
        sequence="AUGCUA",
        structure="(((...)))",
        energy=-32.5,
        runtime=2.4,
        memory=512.0,
        metadata=("version=2.6",),
    )

    assert result.method_name == ("vienna_rna")

    assert result.sequence == ("AUGCUA")

    assert result.structure == ("(((...)))")

    assert result.energy == -32.5

    assert result.runtime == 2.4
