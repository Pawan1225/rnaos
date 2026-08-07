"""
Tests for publication package model.
"""

from validation.models.publication_package import (
    PublicationPackage,
)


def test_publication_package():

    package = PublicationPackage(
        package_id="PACKAGE_001",
        title=("RNAOS Benchmark Publication Package"),
        benchmark_version="1.0.0",
        sections=(
            "Abstract",
            "Methodology",
            "Results",
        ),
        figures=("accuracy_analysis.png",),
        datasets=("RNA_Benchmark_v1",),
        version="1.0.0",
    )

    assert package.package_id == ("PACKAGE_001")

    assert "Results" in package.sections

    assert package.version == ("1.0.0")
