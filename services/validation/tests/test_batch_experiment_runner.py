"""
Tests for batch experiment runner.
"""

from validation.runners.batch_experiment_runner import (
    BatchExperimentRunner,
)


def test_batch_execution() -> None:
    """
    Batch execution works.
    """

    runner = BatchExperimentRunner()

    result = runner.run(
        (
            "AUGCUA",
            "GGGAAA",
            "UUCCGG",
        )
    )

    assert result.batch_id == ("BATCH_001")

    assert result.total_sequences == 3

    assert result.completed_sequences == 3

    assert result.failed_sequences == 0

    assert result.version == ("1.0.0")
