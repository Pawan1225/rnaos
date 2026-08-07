"""
RNAOS benchmark execution runner.
"""

from __future__ import annotations

from dl.benchmark.adapters.base_adapter import (
    BenchmarkAdapter,
)
from dl.models.benchmark.benchmark_case import (
    BenchmarkCase,
)


class BenchmarkRunner:
    """
    Executes benchmark cases.
    """

    def __init__(
        self,
        adapters: tuple[
            BenchmarkAdapter,
            ...,
        ],
    ) -> None:
        self._adapters = adapters

    def run(
        self,
        case: BenchmarkCase,
    ) -> tuple:
        """
        Execute benchmark case.
        """

        results = []

        for adapter in self._adapters:
            result = adapter.run(
                case.sequence,
            )

            results.append(
                result,
            )

        return tuple(results)
