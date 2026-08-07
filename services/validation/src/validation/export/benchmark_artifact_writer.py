"""
RNAOS large benchmark artifact writer.

Persists benchmark campaign outputs.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path


class BenchmarkArtifactWriter:
    """
    Writes RNAOS benchmark artifacts.
    """

    def __init__(
        self,
        output_dir: str,
    ) -> None:
        self.output_dir = Path(output_dir)

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def write_results(
        self,
        results: list[dict],
    ) -> None:
        """
        Write experiment results.
        """

        path = self.output_dir / "experiment_results.json"

        path.write_text(
            json.dumps(
                results,
                indent=2,
            )
        )

    def write_summary(
        self,
        summary: dict,
    ) -> None:
        """
        Write benchmark summary.
        """

        path = self.output_dir / "benchmark_summary.json"

        path.write_text(
            json.dumps(
                summary,
                indent=2,
            )
        )

    def write_manifest(
        self,
        metadata: dict,
    ) -> None:
        """
        Write reproducibility manifest.
        """

        manifest = {
            "created_at": (datetime.now(UTC).isoformat()),
            **metadata,
        }

        path = self.output_dir / "manifest.json"

        path.write_text(
            json.dumps(
                manifest,
                indent=2,
            )
        )
