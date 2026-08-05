from cloud.artifacts import (
    Artifact,
    ArtifactKind,
    ArtifactStore,
)


def test_save_artifact():
    store = ArtifactStore()

    artifact = Artifact(
        name="Benchmark Report",
        kind=ArtifactKind.REPORT,
        data="# RNAOS Report",
    )

    store.save(artifact)

    assert store.count() == 1


def test_get_artifact():
    store = ArtifactStore()

    artifact = Artifact(
        name="RNA Model",
        kind=ArtifactKind.MODEL,
        data={"accuracy": 0.95},
    )

    store.save(artifact)

    loaded = store.get(artifact.artifact_id)

    assert loaded is not None
    assert loaded.name == "RNA Model"
    assert loaded.kind == ArtifactKind.MODEL


def test_remove_artifact():
    store = ArtifactStore()

    artifact = Artifact(
        name="Runtime Plot",
        kind=ArtifactKind.PLOT,
        data="plot.png",
    )

    store.save(artifact)

    store.remove(artifact.artifact_id)

    assert store.count() == 0


def test_list_artifacts():
    store = ArtifactStore()

    artifact_a = Artifact(
        name="A",
        kind=ArtifactKind.REPORT,
        data=None,
    )

    artifact_b = Artifact(
        name="B",
        kind=ArtifactKind.MODEL,
        data=None,
    )

    store.save(artifact_a)
    store.save(artifact_b)

    artifacts = store.list()

    assert len(artifacts) == 2

    ids = {artifact.artifact_id for artifact in artifacts}

    assert artifact_a.artifact_id in ids
    assert artifact_b.artifact_id in ids


def test_missing_artifact():
    store = ArtifactStore()

    assert store.get("missing") is None


def test_overwrite_artifact():
    store = ArtifactStore()

    artifact = Artifact(
        name="Experiment",
        kind=ArtifactKind.REPORT,
        data="v1",
    )

    store.save(artifact)

    updated = Artifact(
        artifact_id=artifact.artifact_id,
        name="Experiment",
        kind=ArtifactKind.REPORT,
        data="v2",
    )

    store.save(updated)

    loaded = store.get(artifact.artifact_id)

    assert loaded is not None
    assert loaded.data == "v2"
