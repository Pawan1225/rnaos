from cloud.cache import DistributedCache


def test_put_value():
    cache = DistributedCache()

    cache.put(
        "rna-1",
        "ACGU",
    )

    assert cache.count() == 1


def test_get_value():
    cache = DistributedCache()

    cache.put(
        "model",
        {"accuracy": 0.95},
    )

    value = cache.get("model")

    assert value == {"accuracy": 0.95}


def test_missing_key():
    cache = DistributedCache()

    assert cache.get("missing") is None


def test_remove_value():
    cache = DistributedCache()

    cache.put(
        "plot",
        "plot.png",
    )

    cache.remove("plot")

    assert cache.count() == 0

    assert cache.get("plot") is None


def test_clear_cache():
    cache = DistributedCache()

    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)

    assert cache.count() == 3

    cache.clear()

    assert cache.count() == 0


def test_overwrite_value():
    cache = DistributedCache()

    cache.put(
        "experiment",
        "v1",
    )

    cache.put(
        "experiment",
        "v2",
    )

    assert cache.count() == 1

    assert cache.get("experiment") == "v2"


def test_cache_multiple_entries():
    cache = DistributedCache()

    for i in range(10):
        cache.put(
            f"key-{i}",
            i,
        )

    assert cache.count() == 10

    for i in range(10):
        assert cache.get(f"key-{i}") == i


def test_namespaces_are_isolated():
    cache = DistributedCache()

    cache.put(
        "embedding",
        "model-a",
        namespace="models",
    )

    cache.put(
        "embedding",
        "dataset-a",
        namespace="datasets",
    )

    assert (
        cache.get(
            "embedding",
            namespace="models",
        )
        == "model-a"
    )

    assert (
        cache.get(
            "embedding",
            namespace="datasets",
        )
        == "dataset-a"
    )


def test_default_namespace():
    cache = DistributedCache()

    cache.put(
        "key",
        "value",
    )

    assert cache.get("key") == "value"


def test_cache_statistics():
    cache = DistributedCache()

    cache.put(
        "rna",
        "ACGU",
    )

    assert cache.get("rna") == "ACGU"

    assert cache.get("missing") is None

    stats = cache.statistics()

    assert stats.hits == 1
    assert stats.misses == 1
    assert stats.requests == 2
    assert stats.hit_ratio == 0.5


def test_empty_statistics():
    cache = DistributedCache()

    stats = cache.statistics()

    assert stats.requests == 0
    assert stats.hit_ratio == 0.0


def test_put_if_absent():
    cache = DistributedCache()

    assert cache.put_if_absent("key", 1)

    assert not cache.put_if_absent("key", 2)

    assert cache.get("key") == 1


def test_replace():
    cache = DistributedCache()

    assert not cache.replace("key", 2)

    cache.put("key", 1)

    assert cache.replace("key", 2)

    assert cache.get("key") == 2


def test_compare_and_swap():
    cache = DistributedCache()

    cache.put("counter", 1)

    assert cache.compare_and_swap(
        "counter",
        expected_value=1,
        new_value=2,
    )

    assert cache.get("counter") == 2

    assert not cache.compare_and_swap(
        "counter",
        expected_value=1,
        new_value=3,
    )

    assert cache.get("counter") == 2


def test_compare_and_swap_missing_key():
    cache = DistributedCache()

    assert not cache.compare_and_swap(
        "missing",
        expected_value=1,
        new_value=2,
    )


def test_replace_preserves_missing_key():
    cache = DistributedCache()

    assert not cache.replace("missing", 10)

    assert cache.get("missing") is None


def test_put_if_absent_does_not_overwrite():
    cache = DistributedCache()

    assert cache.put_if_absent("experiment", "v1")

    assert not cache.put_if_absent("experiment", "v2")

    assert cache.get("experiment") == "v1"
