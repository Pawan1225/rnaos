"""
Tests for release artifact generator.
"""

from __future__ import annotations

from dl.submission.release.release_artifact_generator import (
    ReleaseArtifactGenerator,
)


def test_release_generation() -> None:
    """
    Release manifest is generated.
    """

    generator = ReleaseArtifactGenerator()

    manifest = generator.generate()

    assert manifest.release_id == ("RELEASE_001")

    assert manifest.version == ("1.0.0")

    assert "scientific_report" in manifest.artifacts

    assert manifest.checksum_file == ("checksums.txt")
