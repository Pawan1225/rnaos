from validation.analyzers.runtime_scaling_generator import (
    RuntimeScalingGenerator,
)


def test_runtime_scaling_generation():

    results = [
        {
            "sequence_length": 20,
            "runtime_seconds": 0.1,
        },
        {
            "sequence_length": 20,
            "runtime_seconds": 0.3,
        },
        {
            "sequence_length": 40,
            "runtime_seconds": 0.5,
        },
    ]

    generator = RuntimeScalingGenerator()

    report = generator.generate(results)

    assert report["metric"] == ("runtime_scaling")

    assert report["total_samples"] == 3

    assert report["average_runtime"] == 0.3

    assert report["scaling_by_length"]["20"] == 0.2
