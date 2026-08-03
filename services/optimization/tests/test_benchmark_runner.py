from optimization.benchmark import BenchmarkRunner


def test_single_sequence() -> None:
    runner = BenchmarkRunner()

    result = runner.run(
        "GGGAAAUCC",
    )

    assert result.qubo_size > 0

    assert result.candidate_pairs > 0

    assert result.runtime_seconds >= 0.0


def test_batch() -> None:
    runner = BenchmarkRunner()

    results = runner.run_batch(
        [
            "GGGAAAUCC",
            "AUGCGGAU",
            "GGCCAAUU",
        ]
    )

    assert len(results) == 3
