from validation.export.experiment_result_serializer import (
    ExperimentResultSerializer,
)
from validation.models.experiment_result import (
    ExperimentResult,
)


def test_experiment_result_serialization():

    result = ExperimentResult(
        experiment_id=1,
        sequence_id="RNA_20_001",
        sequence="GGCAU",
        sequence_length=5,
        rnaos_structure="(((...)))",
        reference_structure="(((...)))",
        rnaos_energy=-1.0,
        reference_energy=-1.2,
        energy_gap=0.2,
        accuracy=0.95,
        runtime_seconds=0.1,
        estimated_qubits=10,
    )

    serializer = ExperimentResultSerializer()

    output = serializer.serialize(result)

    assert output["experiment_id"] == 1
    assert output["sequence"] == "GGCAU"
    assert output["accuracy"] == 0.95
    assert output["estimated_qubits"] == 10
