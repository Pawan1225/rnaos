from rnaos_platform.config import ConfigManager


def test_set_get() -> None:
    config = ConfigManager()

    config.set(
        "solver.iterations",
        500,
    )

    assert config.get("solver.iterations") == 500


def test_exists() -> None:
    config = ConfigManager()

    config.set(
        "platform.mode",
        "development",
    )

    assert config.exists(
        "platform.mode",
    )


def test_remove() -> None:
    config = ConfigManager()

    config.set(
        "x",
        1,
    )

    config.remove("x")

    assert not config.exists("x")


def test_all() -> None:
    config = ConfigManager()

    config.set(
        "a",
        1,
    )

    config.set(
        "b",
        2,
    )

    assert len(config.all()) == 2


def test_default_value() -> None:
    config = ConfigManager()

    assert (
        config.get(
            "missing.key",
            "default",
        )
        == "default"
    )
