from cloud.execution.worker import Worker
from cloud.execution.worker_registry import WorkerRegistry
from cloud.execution.worker_state import WorkerState


def test_register_worker():
    registry = WorkerRegistry()

    registry.register(
        Worker(
            worker_id="worker-1",
            hostname="node1",
        )
    )

    assert registry.worker_count() == 1


def test_unregister_worker():
    registry = WorkerRegistry()

    worker = Worker(
        worker_id="worker-1",
        hostname="node1",
    )

    registry.register(worker)

    registry.unregister("worker-1")

    assert registry.worker_count() == 0


def test_lookup_worker():
    registry = WorkerRegistry()

    worker = Worker(
        worker_id="worker-1",
        hostname="node1",
    )

    registry.register(worker)

    assert registry.get("worker-1") is worker


def test_filter_by_capability():
    registry = WorkerRegistry()

    registry.register(
        Worker(
            worker_id="gpu-1",
            hostname="gpu-node",
            capabilities={"gpu"},
        )
    )

    registry.register(
        Worker(
            worker_id="cpu-1",
            hostname="cpu-node",
            capabilities={"cpu"},
        )
    )

    workers = registry.by_capability("gpu")

    assert len(workers) == 1
    assert workers[0].worker_id == "gpu-1"


def test_filter_by_state():
    registry = WorkerRegistry()

    worker = Worker(
        worker_id="worker-1",
        hostname="node1",
    )

    worker.state = WorkerState.BUSY

    registry.register(worker)

    workers = registry.by_state(WorkerState.BUSY)

    assert len(workers) == 1
    assert workers[0].worker_id == "worker-1"


def test_workers_sorted():
    registry = WorkerRegistry()

    registry.register(
        Worker(
            worker_id="b",
            hostname="b-node",
        )
    )

    registry.register(
        Worker(
            worker_id="a",
            hostname="a-node",
        )
    )

    workers = registry.list_workers()

    assert workers[0].worker_id == "a"
    assert workers[1].worker_id == "b"
