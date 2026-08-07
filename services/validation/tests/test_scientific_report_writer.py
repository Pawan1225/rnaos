from pathlib import Path

from validation.export.scientific_report_writer import (
    ScientificReportWriter,
)


def test_scientific_report_writer(
    tmp_path: Path,
):

    writer = ScientificReportWriter(str(tmp_path))

    report = {
        "benchmark": "RNAOS_LARGE_V1",
        "experiments": 400,
        "accuracy": {
            "mean": 0.94,
        },
    }

    path = writer.write(report)

    assert path.exists()

    content = path.read_text()

    assert "RNAOS_LARGE_V1" in content
