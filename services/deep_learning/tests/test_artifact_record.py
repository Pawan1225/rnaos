"""
Tests for artifact record.
"""

from __future__ import annotations

from dl.models.submission.artifact_record import (
    ArtifactRecord,
)


def test_artifact_record() -> None:
    """
    Artifact contract creation works.
    """

    artifact = ArtifactRecord(
        artifact_id="ARTIFACT_001",
        artifact_type="SCIENTIFIC_REPORT",
        artifact_name="RNAOS Report",
        version="1.0.0",
        location="reports/report.pdf",
        generator="ScientificReportGenerator",
        created_at="2026-08-07",
        checksum="sha256:test",
        metadata=("benchmark=v14.7",),
    )

    assert artifact.artifact_id == ("ARTIFACT_001")

    assert artifact.artifact_type == ("SCIENTIFIC_REPORT")

    assert artifact.version == ("1.0.0")
