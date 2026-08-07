"""
Tests for result summary generator.
"""

from __future__ import annotations

from dl.benchmark.reporting.result_summary_generator import (
    ResultSummaryGenerator,
)


def test_result_summary_generator() -> None:
    """
    Summary generation works.
    """

    generator = ResultSummaryGenerator()

    summary = generator.generate()

    assert summary.best_method == ("rnaos_hybrid")

    assert summary.best_accuracy == 0.95

    assert summary.best_energy == -35.0

    assert summary.runtime_improvement == 0.20

    assert (
        len(
            summary.key_findings,
        )
        == 3
    )
