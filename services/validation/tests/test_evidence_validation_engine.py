from validation.release.evidence_validation_engine import (
    EvidenceValidationEngine,
)


def test_evidence_validation(
    tmp_path,
):

    package = tmp_path

    figures = package / "figures"

    validation = package / "validation"

    figures.mkdir()
    validation.mkdir()

    required = {
        "accuracy_vs_length.png",
        "energy_gap_distribution.png",
        "runtime_scaling.png",
        "quantum_resource_scaling.png",
    }

    for file in required:
        (figures / file).write_text("figure")

    (validation / "scientific_report.json").write_text("{}")

    (package / "package_manifest.json").write_text("{}")

    engine = EvidenceValidationEngine()

    result = engine.validate(str(package))

    assert result["status"] == ("VALIDATED")
