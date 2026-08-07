"""
Tests for benchmark execution system.
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
from dl.benchmark.validation.execution_validator import (
    ExecutionValidator,
)
from dl.models.benchmark.benchmark_case import (
    BenchmarkCase,
)


def test_complete_execution_pipeline() -> None:
    """
    Complete benchmark execution works.
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

    validator = ExecutionValidator()

    assert validator.validate(
        case,
    )

    runner = BenchmarkRunner(
        adapters=(
            ViennaRNAAdapter(),
            RNAOSAdapter(),
        ),
    )

    results = runner.run(
        case,
    )

    assert len(results) == 2

    assert results[0].method_name == ("vienna_rna")

    assert results[1].method_name == ("rnaos_hybrid")


def test_invalid_case_blocked() -> None:
    """
    Invalid benchmark case is rejected.
    """

    case = BenchmarkCase(
        case_id="",
        sequence="XYZ",
        reference_structure="",
        reference_energy=0.0,
        methods=(),
        metadata=(),
    )

    validator = ExecutionValidator()

    assert not validator.validate(
        case,
    )
