"""
RNAOS scientific report writer.

Persists benchmark statistics
as a scientific evidence artifact.
"""

from __future__ import annotations

import json
from pathlib import Path


class ScientificReportWriter:
    """
    Writes scientific benchmark reports.
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

    def write(
        self,
        report: dict,
    ) -> Path:
        """
        Write scientific report JSON.
        """

        path = self.output_dir / "scientific_report.json"

        path.write_text(
            json.dumps(
                report,
                indent=2,
            )
        )

        return path
