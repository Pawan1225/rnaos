from enterprise.benchmark import (
    BenchmarkCategory,
    BenchmarkRegistry,
    BenchmarkResult,
    BenchmarkStatus,
)


class BenchmarkOne:
    @property
    def name(self) -> str:
        return "RNA"

    def run(self) -> BenchmarkResult:
        return BenchmarkResult(
            name=self.name,
            status=BenchmarkStatus.PASSED,
            category=BenchmarkCategory.PLATFORM,
            runtime_seconds=0.1,
        )


class BenchmarkTwo:
    @property
    def name(self) -> str:
        return "Cloud"

    def run(self) -> BenchmarkResult:
        return BenchmarkResult(
            name=self.name,
            status=BenchmarkStatus.PASSED,
            category=BenchmarkCategory.PLATFORM,
            runtime_seconds=0.2,
        )


def test_register():
    registry = BenchmarkRegistry()

    registry.register(BenchmarkOne())

    assert registry.count() == 1


def test_lookup():
    registry = BenchmarkRegistry()

    benchmark = BenchmarkOne()

    registry.register(benchmark)

    assert registry.get("RNA") is benchmark


def test_exists():
    registry = BenchmarkRegistry()

    registry.register(BenchmarkTwo())

    assert registry.exists("Cloud")


def test_remove():
    registry = BenchmarkRegistry()

    registry.register(BenchmarkTwo())

    registry.remove("Cloud")

    assert registry.count() == 0


def test_clear():
    registry = BenchmarkRegistry()

    registry.register(BenchmarkOne())
    registry.register(BenchmarkTwo())

    registry.clear()

    assert registry.count() == 0


def test_list():
    registry = BenchmarkRegistry()

    registry.register(BenchmarkTwo())
    registry.register(BenchmarkOne())

    assert registry.list_benchmarks() == [
        "Cloud",
        "RNA",
    ]


def test_items():
    registry = BenchmarkRegistry()

    benchmark = BenchmarkOne()

    registry.register(benchmark)

    items = registry.items()

    assert len(items) == 1
    assert items[0] is benchmark
    assert items[0].name == "RNA"
