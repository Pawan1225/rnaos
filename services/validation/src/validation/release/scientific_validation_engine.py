"""
RNAOS scientific validation engine.

Validates frozen benchmark evidence.
"""

from __future__ import annotations


class ScientificValidationEngine:
    """
    Validates scientific benchmark package.
    """

    REQUIRED_ARTIFACTS = {
        "experiment_results.json",
        "benchmark_summary.json",
        "accuracy_analysis.json",
        "energy_gap_analysis.json",
        "runtime_scaling.json",
        "quantum_resource_scaling.json",
        "manifest.json",
    }

    REQUIRED_FIELDS = {
        "experiment_id",
        "sequence",
        "sequence_length",
        "rnaos_structure",
        "reference_structure",
        "rnaos_energy",
        "reference_energy",
        "energy_gap",
        "accuracy",
        "runtime_seconds",
        "estimated_qubits",
    }

    def validate(
        self,
        results: list[dict],
        artifacts: list[str],
        manifest: dict,
    ) -> dict:
        """
        Validate benchmark package.
        """

        self._validate_results(results)

        self._validate_artifacts(artifacts)

        self._validate_manifest(manifest)

        return {
            "status": "VALIDATED",
            "experiments": len(results),
            "artifacts": len(artifacts),
        }

    def _validate_results(
        self,
        results: list[dict],
    ) -> None:

        if len(results) != 400:
            raise ValueError("Expected 400 experiments")

        for result in results:
            missing = self.REQUIRED_FIELDS - result.keys()

            if missing:
                raise ValueError(f"Missing fields: {missing}")

    def _validate_artifacts(
        self,
        artifacts: list[str],
    ) -> None:

        missing = self.REQUIRED_ARTIFACTS - set(artifacts)

        if missing:
            raise ValueError(f"Missing artifacts: {missing}")

    def _validate_manifest(
        self,
        manifest: dict,
    ) -> None:

        if manifest.get("status") != "FROZEN":
            raise ValueError("Benchmark not frozen")
