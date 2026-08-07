"""
Tests for reproducibility generator.
"""

from __future__ import annotations

from dl.submission.reproducibility.reproducibility_generator import (
    ReproducibilityGenerator,
)


def test_reproducibility_generation() -> None:
    """
    Reproducibility manifest is generated.
    """

    generator = ReproducibilityGenerator()

    manifest = generator.generate()

    assert manifest.reproducibility_id == ("REPRO_001")

    assert "environment.yml" in manifest.files

    assert "random_seed=42" in manifest.seeds

    assert manifest.version == ("1.0.0")
