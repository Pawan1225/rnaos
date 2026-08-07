"""
RNAOS scientific evidence generation runner.
"""

from __future__ import annotations

import json
import shutil
import sys
from dataclasses import asdict
from pathlib import Path


def setup_import_path() -> None:
    """
    Add validation src directory to Python path.
    """

    src_path = Path(__file__).resolve().parents[1] / "src"

    sys.path.insert(
        0,
        str(src_path),
    )


def main() -> None:
    """
    Generate scientific evidence artifacts.
    """

    setup_import_path()

    from validation.analyzers.accuracy_analysis_generator import (
        AccuracyAnalysisGenerator,
    )
    from validation.analyzers.energy_gap_analysis_generator import (
        EnergyGapAnalysisGenerator,
    )
    from validation.analyzers.quantum_resource_analysis_generator import (
        QuantumResourceAnalysisGenerator,
    )
    from validation.analyzers.runtime_scaling_analysis_engine import (
        RuntimeScalingAnalysisEngine,
    )
    from validation.reports.scientific_report_generator import (
        ScientificReportGenerator,
    )

    print("Starting Scientific Evidence Generation")

    source_dir = Path("validation_results/large_benchmark_v1")

    evidence_dir = Path("wiser_submission/06_experimental_evidence/large_benchmark_v1")

    results_file = source_dir / "experiment_results.json"

    results = json.loads(results_file.read_text())

    print(f"Loaded experiments: {len(results)}")

    evidence_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    # Accuracy Analysis

    accuracy = AccuracyAnalysisGenerator().generate(results)

    (source_dir / "accuracy_analysis.json").write_text(
        json.dumps(
            accuracy,
            indent=2,
        )
    )

    # Energy Gap Analysis

    energy = EnergyGapAnalysisGenerator().generate(results)

    (source_dir / "energy_gap_analysis.json").write_text(
        json.dumps(
            energy,
            indent=2,
        )
    )

    # Runtime Scaling

    runtimes = tuple(item["runtime_seconds"] for item in results)

    runtime = RuntimeScalingAnalysisEngine().analyze(runtimes)

    (source_dir / "runtime_scaling.json").write_text(
        json.dumps(
            asdict(runtime),
            indent=2,
        )
    )

    # Quantum Resource Analysis

    quantum = QuantumResourceAnalysisGenerator().generate(results)

    (source_dir / "quantum_resource_scaling.json").write_text(
        json.dumps(
            asdict(quantum),
            indent=2,
        )
    )

    # Scientific Report

    report = ScientificReportGenerator().generate()

    (source_dir / "scientific_report.json").write_text(
        json.dumps(
            asdict(report),
            indent=2,
        )
    )

    # Copy generated evidence

    files = (
        "scientific_report.json",
        "accuracy_analysis.json",
        "energy_gap_analysis.json",
        "runtime_scaling.json",
        "quantum_resource_scaling.json",
    )

    for filename in files:
        shutil.copy(
            source_dir / filename,
            evidence_dir / filename,
        )

    print("Scientific Evidence Generated")

    for filename in files:
        print(filename)


if __name__ == "__main__":
    main()
