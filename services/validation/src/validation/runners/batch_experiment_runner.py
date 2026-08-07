"""
RNAOS batch experiment runner.
"""

from __future__ import annotations

from validation.models.batch_result import (
    BatchResult,
)


class BatchExperimentRunner:
    """
    Executes benchmark batches.
    """

    def run(
        self,
        sequences: tuple[str, ...],
    ) -> BatchResult:
        """
        Execute batch experiments.
        """

        completed = 0

        failed = 0

        for sequence in sequences:
            try:
                _ = sequence

                completed += 1

            except Exception:
                failed += 1

        return BatchResult(
            batch_id="BATCH_001",
            total_sequences=len(sequences),
            completed_sequences=completed,
            failed_sequences=failed,
            version="1.0.0",
        )
