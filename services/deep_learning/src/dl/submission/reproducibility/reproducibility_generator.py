"""
RNAOS reproducibility package generator.
"""

from __future__ import annotations

from dl.models.submission.reproducibility_manifest import (
    ReproducibilityManifest,
)


class ReproducibilityGenerator:
    """
    Generates reproducibility manifests.
    """

    def generate(
        self,
    ) -> ReproducibilityManifest:
        """
        Create reproducibility definition.
        """

        return ReproducibilityManifest(
            reproducibility_id="REPRO_001",
            files=(
                "environment.yml",
                "requirements.txt",
                "run_experiment.sh",
                "README.md",
            ),
            environment=("python_3.11"),
            dependencies=(
                "numpy",
                "torch",
                "pennylane",
                "scikit-learn",
            ),
            configs=(
                "benchmark_config.yaml",
                "model_config.yaml",
            ),
            seeds=("random_seed=42",),
            version="1.0.0",
            metadata=("release=RNAOS_v1",),
        )
