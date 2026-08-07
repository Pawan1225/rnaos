"""
Tests for report metadata.
"""

from __future__ import annotations

from dl.models.benchmark.report_metadata import (
    ReportMetadata,
)


def test_report_metadata() -> None:
    """
    Report metadata can be created.
    """

    metadata = ReportMetadata(
        software_version="14.7.0",
        model_versions=(
            "ml_v1",
            "dl_v2",
        ),
        hardware="Apple M-Series",
        runtime_environment="Python 3.11",
        dataset_version="Rfam-v1",
        random_seed=42,
        timestamp="2026-08-07",
    )

    assert metadata.software_version == ("14.7.0")

    assert metadata.dataset_version == ("Rfam-v1")

    assert metadata.random_seed == 42

    assert (
        len(
            metadata.model_versions,
        )
        == 2
    )
