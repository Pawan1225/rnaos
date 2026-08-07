"""
RNAOS benchmark adapter.
"""

from __future__ import annotations

import time

from dl.benchmark.adapters.base_adapter import (
    BenchmarkAdapter,
)
from dl.models.benchmark.adapter_result import (
    BenchmarkAdapterResult,
)


class RNAOSAdapter(BenchmarkAdapter):
    """
    Adapter for RNAOS hybrid optimizer.
    """

    @property
    def name(
        self,
    ) -> str:
        """
        Adapter name.
        """

        return "rnaos_hybrid"

    def run(
        self,
        sequence: str,
    ) -> BenchmarkAdapterResult:
        """
        Execute RNAOS optimization.
        """

        start = time.perf_counter()

        # Placeholder connection point.
        # Future:
        # HybridOptimizationEngine will be called here.

        structure = "(....)"

        energy = -2.0

        runtime = time.perf_counter() - start

        return BenchmarkAdapterResult(
            method_name=self.name,
            sequence=sequence,
            structure=structure,
            energy=energy,
            runtime=runtime,
            memory=0.0,
            metadata=(
                "engine=hybrid_optimizer",
                "version=14.6",
            ),
        )
