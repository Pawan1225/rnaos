from validation.release.freeze_manifest_generator import (
    FreezeManifestGenerator,
)


def test_freeze_manifest_generation():

    generator = FreezeManifestGenerator()

    manifest = generator.generate(
        {
            "benchmark_id": ("RNAOS_BENCHMARK_V1"),
            "total_experiments": 400,
        },
        [
            "experiment_results.json",
            "benchmark_summary.json",
        ],
    )

    assert manifest["status"] == "FROZEN"

    assert manifest["experiments"] == 400

    assert len(manifest["artifacts"]) == 2
