from cloud.scheduler.compute_resource import ComputeResource
from cloud.scheduler.resource_kind import ResourceKind
from cloud.scheduler.resource_registry import ResourceRegistry


def test_register_resource():
    registry = ResourceRegistry()

    registry.register(
        ComputeResource(
            resource_id="cpu-1",
            hostname="node1",
            kind=ResourceKind.CPU,
            capacity=32,
        )
    )

    assert registry.resource_count() == 1


def test_unregister_resource():
    registry = ResourceRegistry()

    resource = ComputeResource(
        resource_id="cpu-1",
        hostname="node1",
        kind=ResourceKind.CPU,
        capacity=32,
    )

    registry.register(resource)

    registry.unregister("cpu-1")

    assert registry.resource_count() == 0


def test_lookup_resource():
    registry = ResourceRegistry()

    resource = ComputeResource(
        resource_id="gpu-1",
        hostname="gpu01",
        kind=ResourceKind.GPU,
        capacity=4,
    )

    registry.register(resource)

    assert registry.get("gpu-1") is resource


def test_filter_by_kind():
    registry = ResourceRegistry()

    registry.register(
        ComputeResource(
            resource_id="cpu-1",
            hostname="cpu01",
            kind=ResourceKind.CPU,
            capacity=32,
        )
    )

    registry.register(
        ComputeResource(
            resource_id="gpu-1",
            hostname="gpu01",
            kind=ResourceKind.GPU,
            capacity=4,
        )
    )

    resources = registry.by_kind(ResourceKind.GPU)

    assert len(resources) == 1
    assert resources[0].resource_id == "gpu-1"


def test_available_resources():
    registry = ResourceRegistry()

    registry.register(
        ComputeResource(
            resource_id="cpu-1",
            hostname="node1",
            kind=ResourceKind.CPU,
            capacity=32,
            available=True,
        )
    )

    registry.register(
        ComputeResource(
            resource_id="cpu-2",
            hostname="node2",
            kind=ResourceKind.CPU,
            capacity=32,
            available=False,
        )
    )

    resources = registry.available(ResourceKind.CPU)

    assert len(resources) == 1
    assert resources[0].resource_id == "cpu-1"


def test_resources_sorted():
    registry = ResourceRegistry()

    registry.register(
        ComputeResource(
            resource_id="b",
            hostname="node-b",
            kind=ResourceKind.CPU,
            capacity=8,
        )
    )

    registry.register(
        ComputeResource(
            resource_id="a",
            hostname="node-a",
            kind=ResourceKind.CPU,
            capacity=8,
        )
    )

    resources = registry.list_resources()

    assert resources[0].resource_id == "a"
    assert resources[1].resource_id == "b"
