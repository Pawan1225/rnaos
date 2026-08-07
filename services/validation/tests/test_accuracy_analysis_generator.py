from validation.analyzers.accuracy_analysis_generator import (
    AccuracyAnalysisGenerator,
)


def test_accuracy_analysis_generation():

    results = [
        {
            "sequence_length": 20,
            "accuracy": 0.90,
        },
        {
            "sequence_length": 20,
            "accuracy": 1.00,
        },
        {
            "sequence_length": 40,
            "accuracy": 0.95,
        },
    ]

    generator = AccuracyAnalysisGenerator()

    report = generator.generate(results)

    assert report["metric"] == "accuracy"

    assert report["total_samples"] == 3

    assert report["average_accuracy"] == 0.95

    assert report["accuracy_distribution"]["20"] == 0.95
