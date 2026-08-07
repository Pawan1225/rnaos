"""
RNAOS evidence package generator.

Creates final scientific submission package.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path


class EvidencePackageGenerator:
    """
    Generates scientific evidence package.
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

    def generate(
        self,
        source_dir: str,
        figure_dir: str,
    ) -> Path:
        """
        Generate evidence package.
        """

        source = Path(source_dir)

        figures = Path(figure_dir)

        validation_dir = self.output_dir / "validation"

        package_figures = self.output_dir / "figures"

        validation_dir.mkdir(
            exist_ok=True,
        )

        package_figures.mkdir(
            exist_ok=True,
        )

        report = source / "scientific_report.json"

        manifest = source / "manifest.json"

        shutil.copy(
            report,
            validation_dir / "scientific_report.json",
        )

        shutil.copy(
            manifest,
            validation_dir / "manifest.json",
        )

        for figure in figures.glob("*.png"):
            shutil.copy(
                figure,
                package_figures / figure.name,
            )

        package_manifest = {
            "package": ("RNAOS_SCIENTIFIC_EVIDENCE_V1"),
            "contents": [
                "figures",
                "validation",
            ],
        }

        (self.output_dir / "package_manifest.json").write_text(
            json.dumps(
                package_manifest,
                indent=2,
            )
        )

        (self.output_dir / "README.md").write_text("# RNAOS Scientific Evidence Package\n")

        return self.output_dir
