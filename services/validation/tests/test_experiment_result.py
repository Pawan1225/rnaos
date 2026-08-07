"""
Tests for experiment result model.
"""

from validation.models.experiment_result import (
    ExperimentResult,
)


def test_experiment_result_creation():

    result = ExperimentResult(
        experiment_id=1,
        sequence_id="RNA_001",
        sequence="GGCAU",
        sequence_length=5,
        rnaos_structure="(((...)))",
        reference_structure="(((...)))",
        rnaos_energy=-5.2,
        reference_energy=-5.5,
        energy_gap=0.3,
        accuracy=0.94,
        runtime_seconds=0.12,
        estimated_qubits=10,
    )

    assert result.experiment_id == 1

    assert result.sequence == "GGCAU"

    assert result.energy_gap == 0.3

    assert result.estimated_qubits == 10
