"""
Tests for RNAOS campaign result exporter.
"""

from validation.export.campaign_result_exporter import (
    CampaignResultExporter,
)
from validation.models.experiment_result import (
    ExperimentResult,
)


def test_campaign_result_export():

    experiment = ExperimentResult(
        experiment_id=1,
        sequence_id="RNA_001",
        sequence="AUGCUA",
        sequence_length=20,
        rnaos_structure="(((...)))",
        reference_structure="(((...)))",
        rnaos_energy=-5.0,
        reference_energy=-5.2,
        energy_gap=0.2,
        accuracy=0.95,
        runtime_seconds=0.1,
        estimated_qubits=40,
    )

    campaign_result = type(
        "CampaignResult",
        (),
        {
            "experiment_results": (experiment,),
        },
    )()

    exporter = CampaignResultExporter()

    output = exporter.export(campaign_result)

    assert len(output) == 1

    assert output[0]["experiment_id"] == 1

    assert output[0]["accuracy"] == 0.95

    assert output[0]["estimated_qubits"] == 40

    assert output[0]["status"] == "COMPLETED"
