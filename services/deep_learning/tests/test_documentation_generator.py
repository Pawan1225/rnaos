"""
Tests for documentation generator.
"""

from __future__ import annotations

from dl.submission.documentation.documentation_generator import (
    DocumentationGenerator,
)


def test_documentation_generation() -> None:
    """
    Documentation manifest is generated.
    """

    generator = DocumentationGenerator()

    manifest = generator.generate()

    assert manifest.documentation_id == ("DOC_001")

    assert (
        len(
            manifest.sections,
        )
        == 5
    )

    assert "README.md" in manifest.files
