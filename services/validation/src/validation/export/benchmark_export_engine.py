"""
RNAOS benchmark export engine.
"""

from __future__ import annotations

import json
from pathlib import Path

from validation.models.export_manifest import (
    ExportManifest,
)


class BenchmarkExportEngine:
    """
    Exports benchmark artifacts.
    """

    def export(
        self,
        output_dir: str,
    ) -> ExportManifest:
        """
        Create benchmark export package.
        """

        directory = Path(output_dir)

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        files = (
            "benchmark_results.json",
            "benchmark_table.csv",
            "metrics_summary.json",
            "scaling_results.csv",
        )

        for file_name in files:
            path = directory / file_name

            if file_name.endswith(".json"):
                path.write_text(
                    json.dumps(
                        {
                            "version": "1.0.0",
                        },
                        indent=4,
                    ),
                    encoding="utf-8",
                )

            else:
                path.write_text(
                    "metric,value\n",
                    encoding="utf-8",
                )

        return ExportManifest(
            export_id="EXPORT_001",
            files=files,
            format_versions=(
                "json_v1",
                "csv_v1",
            ),
            benchmark_version="1.0.0",
            metadata=("RNAOS benchmark export",),
        )
