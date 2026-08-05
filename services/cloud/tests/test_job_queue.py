from cloud.queue import (
    Job,
    JobQueue,
    JobStatus,
)


def test_submit_job():
    queue = JobQueue()

    queue.submit(
        Job(
            task="RNA Folding",
        )
    )

    assert queue.pending() == 1


def test_fifo_order():
    queue = JobQueue()

    queue.submit(Job(task="Task A"))

    queue.submit(Job(task="Task B"))

    first = queue.next_job()
    second = queue.next_job()

    assert first is not None
    assert second is not None

    assert first.task == "Task A"
    assert second.task == "Task B"


def test_job_running_status():
    queue = JobQueue()

    queue.submit(Job(task="Optimization"))

    job = queue.next_job()

    assert job is not None
    assert job.status == JobStatus.RUNNING


def test_complete_job():
    queue = JobQueue()

    queue.submit(Job(task="RNA Folding"))

    job = queue.next_job()

    assert job is not None

    queue.complete(job)

    # Immutable jobs remain unchanged.
    assert job.status == JobStatus.RUNNING


def test_empty_queue():
    queue = JobQueue()

    assert queue.next_job() is None


def test_pending_count():
    queue = JobQueue()

    queue.submit(Job(task="Task 1"))
    queue.submit(Job(task="Task 2"))
    queue.submit(Job(task="Task 3"))

    assert queue.pending() == 3

    queue.next_job()

    assert queue.pending() == 2
