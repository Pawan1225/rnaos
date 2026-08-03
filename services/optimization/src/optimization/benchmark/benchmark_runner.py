"""
RNAOS Scientific Benchmark Runner.

Sprint 6.7
"""

from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter

from ai_intelligence.profilers.ai_profiler import AIProfiler
from folding.profilers.folding_profiler import FoldingProfiler
from rna_intelligence.profilers.rna_profiler import RNAProfiler

from optimization.profilers.optimization_profiler import (
    OptimizationProfiler,
)
from optimization.validation import QUBOValidator


@dataclass(slots=True)
class BenchmarkResult:
    """
    Complete benchmark result for one RNA sequence.
    """

    sequence: str

    mfe: float

    estimated_energy: float

    absolute_error: float

    relative_error: float

    candidate_pairs: int

    conflicts: int

    qubo_size: int

    runtime_seconds: float


class BenchmarkRunner:
    """
    End-to-end RNAOS benchmark pipeline.
    """

    def __init__(self) -> None:
        self.rna = RNAProfiler()

        self.ai = AIProfiler()

        self.folding = FoldingProfiler()

        self.optimization = OptimizationProfiler()

        self.validator = QUBOValidator()

    def run(
        self,
        sequence: str,
    ) -> BenchmarkResult:
        start = perf_counter()

        rna = self.rna.profile(sequence)

        ai = self.ai.profile(rna)

        folding = self.folding.profile(sequence)

        optimization = self.optimization.profile(
            ai,
            folding,
        )

        report = self.validator.validate(
            folding,
        )

        runtime = perf_counter() - start

        return BenchmarkResult(
            sequence=sequence,
            mfe=report.vienna_mfe,
            estimated_energy=report.estimated_energy,
            absolute_error=report.absolute_error,
            relative_error=report.relative_error,
            candidate_pairs=report.candidate_pairs,
            conflicts=report.conflicts,
            qubo_size=optimization.qubo.size,
            runtime_seconds=runtime,
        )

    def run_batch(
        self,
        sequences: list[str],
    ) -> list[BenchmarkResult]:
        return [self.run(sequence) for sequence in sequences]
