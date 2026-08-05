from cloud.api import (
    CloudBuilder,
)
from cloud.cluster import (
    ClusterNode,
)
from cloud.execution import (
    Worker,
)
from cloud.scheduler import (
    ComputeResource,
    ResourceKind,
)


def test_builder_creates_cloud():
    cloud = CloudBuilder().build()

    assert cloud.execution is not None
    assert cloud.scheduler is not None
    assert cloud.queue is not None
    assert cloud.artifacts is not None
    assert cloud.cache is not None
    assert cloud.cluster is not None


def test_health():
    cloud = CloudBuilder().build()

    health = cloud.health()

    assert health.healthy


def test_status_initial():
    cloud = CloudBuilder().build()

    status = cloud.status()

    assert status.workers == 0
    assert status.resources == 0
    assert status.pending_jobs == 0
    assert status.artifacts == 0
    assert status.cache_entries == 0
    assert status.cluster_nodes == 0


def test_register_worker():
    cloud = CloudBuilder().build()

    cloud.execution.register_worker(
        Worker(
            worker_id="worker-1",
            hostname="worker01",
        )
    )

    assert cloud.status().workers == 1


def test_register_resource():
    cloud = CloudBuilder().build()

    cloud.scheduler.register(
        ComputeResource(
            resource_id="cpu-1",
            kind=ResourceKind.CPU,
            hostname="compute01",
            capacity=64,
        )
    )

    assert cloud.status().resources == 1


def test_cluster_registration():
    cloud = CloudBuilder().build()

    cloud.cluster.register(
        ClusterNode(
            identifier="node-1",
            hostname="compute01",
            cpu_cores=64,
            memory_gb=256,
        )
    )

    status = cloud.status()

    assert status.cluster_nodes == 1


def test_cache():
    cloud = CloudBuilder().build()

    cloud.cache.put(
        "rna",
        "ACGU",
    )

    assert cloud.cache.get("rna") == "ACGU"

    assert cloud.status().cache_entries == 1


def test_artifacts():
    cloud = CloudBuilder().build()

    from cloud.artifacts import Artifact

    cloud.artifacts.save(
        Artifact(
            artifact_id="report-1",
            name="Benchmark",
            kind="report",
            data="OK",
        )
    )

    assert cloud.status().artifacts == 1


def test_queue():
    cloud = CloudBuilder().build()

    from cloud.queue import Job

    cloud.queue.submit(
        Job(
            job_id="job-1",
            task="RNA Folding",
        )
    )

    assert cloud.status().pending_jobs == 1


def test_infrastructure_ready():
    cloud = CloudBuilder().build()

    cloud.execution.register_worker(
        Worker(
            worker_id="worker-1",
            hostname="worker01",
        )
    )

    cloud.scheduler.register(
        ComputeResource(
            resource_id="cpu",
            kind=ResourceKind.CPU,
            hostname="compute01",
            capacity=32,
        )
    )

    cloud.cluster.register(
        ClusterNode(
            identifier="node",
            hostname="node01",
        )
    )

    assert cloud.status().infrastructure_ready
