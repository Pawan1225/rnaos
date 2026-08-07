"""
RNAOS ViennaRNA benchmark adapter.
"""

from __future__ import annotations

import time

from dl.benchmark.adapters.base_adapter import (
    BenchmarkAdapter,
)
from dl.models.benchmark.adapter_result import (
    BenchmarkAdapterResult,
)


class ViennaRNAAdapter(BenchmarkAdapter):
    """
    Adapter for ViennaRNA reference method.
    """

    @property
    def name(
        self,
    ) -> str:
        """
        Return adapter name.
        """

        return "vienna_rna"

    def run(
        self,
        sequence: str,
    ) -> BenchmarkAdapterResult:
        """
        Execute ViennaRNA prediction.

        Placeholder implementation until
        ViennaRNA runtime is connected.
        """

        start = time.perf_counter()

        structure = "(....)"

        energy = -1.0

        runtime = time.perf_counter() - start

        return BenchmarkAdapterResult(
            method_name=self.name,
            sequence=sequence,
            structure=structure,
            energy=energy,
            runtime=runtime,
            memory=0.0,
            metadata=("engine=vienna_rna",),
        )
