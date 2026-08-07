from validation.analyzers.energy_gap_analysis_generator import (
    EnergyGapAnalysisGenerator,
)


def test_energy_gap_analysis_generation():

    results = [
        {
            "energy_gap": 0.2,
            "rnaos_energy": -1.0,
            "reference_energy": -1.2,
        },
        {
            "energy_gap": 0.4,
            "rnaos_energy": -2.0,
            "reference_energy": -2.4,
        },
    ]

    generator = EnergyGapAnalysisGenerator()

    report = generator.generate(results)

    assert report["metric"] == "energy_gap"

    assert report["total_samples"] == 2

    assert report["average_gap"] == 0.3

    assert report["minimum_gap"] == 0.2

    assert report["maximum_gap"] == 0.4
