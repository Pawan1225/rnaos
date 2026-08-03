from __future__ import annotations

from statistics import mean

from research.models.benchmark_case import BenchmarkCase


class BenchmarkDataset:
    """
    Collection of RNA benchmark cases.

    Provides storage, lookup, filtering, and summary statistics
    for benchmarking experiments.
    """

    def __init__(self, name: str):
        self.name = name
        self._cases: dict[str, BenchmarkCase] = {}

    def add_case(self, case: BenchmarkCase) -> None:
        """
        Add a benchmark case.

        Raises
        ------
        ValueError
            If the sequence ID already exists.
        """
        if case.sequence_id in self._cases:
            raise ValueError(f"Duplicate benchmark ID: {case.sequence_id}")

        self._cases[case.sequence_id] = case

    def get_case(self, sequence_id: str) -> BenchmarkCase:
        """Return a benchmark case by ID."""
        return self._cases[sequence_id]

    def remove_case(self, sequence_id: str) -> None:
        """Remove a benchmark case."""
        del self._cases[sequence_id]

    def __len__(self) -> int:
        return len(self._cases)

    def __iter__(self):
        """Iterate over benchmark cases."""
        return iter(self._cases.values())

    @property
    def cases(self) -> list[BenchmarkCase]:
        """Return all benchmark cases."""
        return list(self._cases.values())

    def filter(
        self,
        *,
        family: str | None = None,
        source: str | None = None,
        min_length: int | None = None,
        max_length: int | None = None,
    ) -> list[BenchmarkCase]:
        """
        Filter benchmark cases by metadata and sequence length.
        """
        results = self.cases

        if family is not None:
            results = [c for c in results if c.family == family]

        if source is not None:
            results = [c for c in results if c.source == source]

        if min_length is not None:
            results = [c for c in results if c.length >= min_length]

        if max_length is not None:
            results = [c for c in results if c.length <= max_length]

        return results

    @property
    def average_length(self) -> float:
        """Average RNA sequence length."""
        if not self._cases:
            return 0.0

        return mean(case.length for case in self._cases.values())

    @property
    def average_gc_content(self) -> float:
        """Average GC content across all benchmark cases."""
        if not self._cases:
            return 0.0

        return mean(case.gc_content for case in self._cases.values())
