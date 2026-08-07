from pathlib import Path

from validation.export.evidence_package_generator import (
    EvidencePackageGenerator,
)


def test_evidence_package_generation(
    tmp_path: Path,
):

    source = tmp_path / "source"
    figures = tmp_path / "figures"
    output = tmp_path / "package"

    source.mkdir()
    figures.mkdir()

    (source / "scientific_report.json").write_text("{}")

    (source / "manifest.json").write_text("{}")

    (figures / "accuracy.png").write_text("figure")

    generator = EvidencePackageGenerator(str(output))

    package = generator.generate(
        str(source),
        str(figures),
    )

    assert (package / "package_manifest.json").exists()

    assert (package / "figures" / "accuracy.png").exists()
