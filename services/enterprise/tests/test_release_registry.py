from enterprise.release import (
    ReleaseChannel,
    ReleaseRegistry,
    ReleaseResult,
    ReleaseStatus,
)


class ReleaseOne:
    @property
    def version(self) -> str:
        return "1.0.0"

    def release(self) -> ReleaseResult:
        return ReleaseResult(
            version=self.version,
            description="Stable",
            status=ReleaseStatus.PASSED,
            channel=ReleaseChannel.STABLE,
        )


def test_register():
    registry = ReleaseRegistry()

    registry.register(ReleaseOne())

    assert registry.count() == 1


def test_lookup():
    registry = ReleaseRegistry()

    release = ReleaseOne()

    registry.register(release)

    assert registry.get("1.0.0") is release


def test_exists():
    registry = ReleaseRegistry()

    registry.register(ReleaseOne())

    assert registry.exists("1.0.0")


def test_remove():
    registry = ReleaseRegistry()

    registry.register(ReleaseOne())

    registry.remove("1.0.0")

    assert registry.count() == 0


def test_clear():
    registry = ReleaseRegistry()

    registry.register(ReleaseOne())

    registry.clear()

    assert registry.count() == 0


def test_list():
    registry = ReleaseRegistry()

    registry.register(ReleaseOne())

    assert registry.list_releases() == [
        "1.0.0",
    ]


def test_items():
    registry = ReleaseRegistry()

    release = ReleaseOne()

    registry.register(release)

    items = registry.items()

    assert len(items) == 1
    assert items[0] is release
