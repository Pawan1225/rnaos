"""
Tests for benchmark runner.
"""

from __future__ import annotations

from dl.benchmark.adapters.rnaos_adapter import (
    RNAOSAdapter,
)
from dl.benchmark.adapters.vienna_adapter import (
    ViennaRNAAdapter,
)
from dl.benchmark.execution.benchmark_runner import (
    BenchmarkRunner,
)
from dl.models.benchmark.benchmark_case import (
    BenchmarkCase,
)


def test_benchmark_runner() -> None:
    """
    Runner executes benchmark adapters.
    """

    runner = BenchmarkRunner(
        adapters=(
            ViennaRNAAdapter(),
            RNAOSAdapter(),
        ),
    )

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

    results = runner.run(
        case,
    )

    assert len(results) == 2

    assert results[0].sequence == ("AUGCUA")

    assert results[1].sequence == ("AUGCUA")

    assert results[0].method_name == ("vienna_rna")

    assert results[1].method_name == ("rnaos_hybrid")
