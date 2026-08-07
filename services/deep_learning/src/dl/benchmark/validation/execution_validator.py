"""
RNAOS benchmark execution validator.
"""

from __future__ import annotations

from dl.models.benchmark.benchmark_case import (
    BenchmarkCase,
)


class ExecutionValidator:
    """
    Validates benchmark execution cases.
    """

    VALID_BASES = {
        "A",
        "U",
        "G",
        "C",
    }

    def validate(
        self,
        case: BenchmarkCase,
    ) -> bool:
        """
        Validate benchmark case.
        """

        if not case.case_id:
            return False

        if not case.sequence:
            return False

        if not set(
            case.sequence,
        ).issubset(
            self.VALID_BASES,
        ):
            return False

        return bool(case.methods)
