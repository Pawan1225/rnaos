"""
RNAOS evidence validation engine.

Validates final scientific evidence package.
"""

from __future__ import annotations

from pathlib import Path


class EvidenceValidationEngine:
    """
    Validates evidence package integrity.
    """

    REQUIRED_FIGURES = {
        "accuracy_vs_length.png",
        "energy_gap_distribution.png",
        "runtime_scaling.png",
        "quantum_resource_scaling.png",
    }

    def validate(
        self,
        package_dir: str,
    ) -> dict:
        """
        Validate evidence package.
        """

        package = Path(package_dir)

        figures = package / "figures"

        validation = package / "validation"

        checks = {}

        checks["figures"] = (
            "PASS" if {item.name for item in figures.iterdir()} >= self.REQUIRED_FIGURES else "FAIL"
        )

        checks["validation_files"] = (
            "PASS" if (validation / "scientific_report.json").exists() else "FAIL"
        )

        checks["manifest"] = "PASS" if (package / "package_manifest.json").exists() else "FAIL"

        status = "VALIDATED" if all(value == "PASS" for value in checks.values()) else "FAILED"

        return {
            "package": ("RNAOS_SCIENTIFIC_EVIDENCE_V1"),
            "status": status,
            "checks": checks,
        }
