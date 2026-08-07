"""
Tests for execution validator.
"""

from __future__ import annotations

from dl.benchmark.validation.execution_validator import (
    ExecutionValidator,
)
from dl.models.benchmark.benchmark_case import (
    BenchmarkCase,
)


def test_valid_execution_case() -> None:
    """
    Valid benchmark case passes.
    """

    case = BenchmarkCase(
        case_id="CASE_001",
        sequence="AUGCUA",
        reference_structure="(((...)))",
        reference_energy=-32.5,
        methods=("vienna_rna",),
        metadata=(),
    )

    validator = ExecutionValidator()

    assert validator.validate(
        case,
    )


def test_invalid_sequence() -> None:
    """
    Invalid RNA sequence fails.
    """

    case = BenchmarkCase(
        case_id="CASE_002",
        sequence="AUGXYZ",
        reference_structure="",
        reference_energy=-1.0,
        methods=("vienna_rna",),
        metadata=(),
    )

    validator = ExecutionValidator()

    assert not validator.validate(
        case,
    )


def test_empty_methods() -> None:
    """
    Missing methods fail.
    """

    case = BenchmarkCase(
        case_id="CASE_003",
        sequence="AUGC",
        reference_structure="",
        reference_energy=-1.0,
        methods=(),
        metadata=(),
    )

    validator = ExecutionValidator()

    assert not validator.validate(
        case,
    )
