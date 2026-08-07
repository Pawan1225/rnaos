"""
Tests for experiment record.
"""

from validation.models.experiment_record import (
    ExperimentRecord,
)


def test_experiment_record_creation() -> None:
    """
    Experiment record creation works.
    """

    record = ExperimentRecord(
        experiment_id="EXP_001",
        timestamp="2026-08-07",
        rna_sequence="AUGCUA",
        sequence_length=6,
        vienna_structure="......",
        vienna_energy=-1.2,
        rnaos_structure="......",
        rnaos_energy=-1.0,
        energy_gap=0.2,
        accuracy=0.95,
        runtime=1.5,
        solver="quantum_inspired",
        qubit_estimate=6,
        variable_count=12,
        iterations=100,
        random_seed=42,
        configuration=("optimizer=qaoa",),
    )

    assert record.experiment_id == "EXP_001"

    assert record.sequence_length == 6

    assert record.random_seed == 42
