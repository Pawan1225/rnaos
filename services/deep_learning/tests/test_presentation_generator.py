"""
Tests for presentation generator.
"""

from __future__ import annotations

from dl.submission.presentation.presentation_generator import (
    PresentationGenerator,
)


def test_presentation_generation() -> None:
    """
    Presentation manifest is generated.
    """

    generator = PresentationGenerator()

    manifest = generator.generate()

    assert manifest.presentation_id == ("PRESENTATION_001")

    assert "Architecture" in manifest.slides

    assert "benchmark_results" in manifest.figures

    assert manifest.version == ("1.0.0")
