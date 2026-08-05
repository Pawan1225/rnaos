from cloud.execution.dispatcher import Dispatcher
from cloud.execution.worker import Worker
from cloud.execution.worker_registry import WorkerRegistry
from cloud.execution.worker_state import WorkerState


def test_select_worker():
    registry = WorkerRegistry()

    registry.register(
        Worker(
            worker_id="worker-1",
            hostname="node1",
        )
    )

    registry.register(
        Worker(
            worker_id="worker-2",
            hostname="node2",
        )
    )

    dispatcher = Dispatcher(registry)

    worker = dispatcher.select_worker()

    assert worker is not None
    assert worker.worker_id == "worker-1"


def test_select_least_loaded():
    registry = WorkerRegistry()

    worker1 = Worker(
        worker_id="worker-1",
        hostname="node1",
        max_jobs=4,
    )

    worker2 = Worker(
        worker_id="worker-2",
        hostname="node2",
        max_jobs=4,
    )

    # Simulate workload using the public API
    worker1.assign_job()
    worker1.assign_job()

    worker2.assign_job()

    registry.register(worker1)
    registry.register(worker2)

    dispatcher = Dispatcher(registry)

    worker = dispatcher.select_worker()

    assert worker is worker2


def test_no_available_workers():
    registry = WorkerRegistry()

    worker = Worker(
        worker_id="worker-1",
        hostname="node1",
    )

    worker.state = WorkerState.OFFLINE

    registry.register(worker)

    dispatcher = Dispatcher(registry)

    assert dispatcher.select_worker() is None
