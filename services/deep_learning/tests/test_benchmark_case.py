"""
Tests for benchmark case.
"""

from __future__ import annotations

from dl.models.benchmark.benchmark_case import (
    BenchmarkCase,
)


def test_benchmark_case() -> None:
    """
    Benchmark case can be created.
    """

    case = BenchmarkCase(
        case_id="CASE_001",
        sequence="AUGCUA",
        reference_structure="(((...)))",
        reference_energy=-32.5,
        methods=(
            "vienna_rna",
            "rnaos_hybrid",
        ),
        metadata=("dataset=Rfam",),
    )

    assert case.case_id == ("CASE_001")

    assert case.sequence == ("AUGCUA")

    assert (
        len(
            case.methods,
        )
        == 2
    )

    assert case.reference_energy == (-32.5)
