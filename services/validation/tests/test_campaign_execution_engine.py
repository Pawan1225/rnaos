"""
Tests for campaign execution engine.
"""

from validation.datasets.large_dataset_generator import (
    LargeDatasetGenerator,
)
from validation.runners.campaign_execution_engine import (
    CampaignExecutionEngine,
)


def test_campaign_execution():

    dataset = LargeDatasetGenerator().generate(
        samples_per_length=5,
        seed=42,
    )

    engine = CampaignExecutionEngine()

    result = engine.run(dataset)

    assert result.campaign_id == ("RNAOS_CAMPAIGN_V1")

    assert result.total_experiments == 20

    assert result.completed_experiments == 20

    assert result.failed_experiments == 0
