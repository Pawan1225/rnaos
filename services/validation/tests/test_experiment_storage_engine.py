"""
Tests for experiment storage engine.
"""

from validation.models.experiment_record import (
    ExperimentRecord,
)
from validation.storage.experiment_storage_engine import (
    ExperimentStorageEngine,
)


def test_experiment_storage(
    tmp_path,
) -> None:
    """
    Experiment record can be stored and loaded.
    """

    engine = ExperimentStorageEngine()

    file_path = tmp_path / "experiment.json"

    record = ExperimentRecord(
        experiment_id="EXP_001",
        timestamp="2026-08-07",
        rna_sequence="AUGCUA",
        sequence_length=6,
        vienna_structure="......",
        vienna_energy=-1.5,
        rnaos_structure="......",
        rnaos_energy=-1.2,
        energy_gap=0.3,
        accuracy=1.0,
        runtime=1.0,
        solver="hybrid_quantum_inspired",
        qubit_estimate=6,
        variable_count=12,
        iterations=100,
        random_seed=42,
        configuration=("optimizer=qaoa",),
    )

    engine.save(
        record,
        str(file_path),
    )

    result = engine.load(
        str(file_path),
    )

    assert result["experiment_id"] == ("EXP_001")

    assert result["energy_gap"] == 0.3
