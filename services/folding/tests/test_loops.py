from folding.thermodynamics import LoopEnergyModel


def test_hairpin() -> None:
    estimate = LoopEnergyModel().hairpin(4)

    assert estimate.loop_type == "hairpin"
    assert estimate.energy > 0


def test_invalid_hairpin() -> None:
    estimate = LoopEnergyModel().hairpin(2)

    assert estimate.loop_type == "invalid"
    assert estimate.energy > 50


def test_internal_loop() -> None:
    estimate = LoopEnergyModel().internal(2, 1)

    assert estimate.loop_type == "internal"
    assert estimate.energy > 0


def test_bulge() -> None:
    model = LoopEnergyModel()

    assert model.bulge_energy(3) > model.bulge_energy(1)


def test_multiloop() -> None:
    model = LoopEnergyModel()

    assert model.multiloop_energy(5) > model.multiloop_energy(2)


def test_hairpin_wrapper() -> None:
    model = LoopEnergyModel()

    assert model.hairpin_energy(5) == model.hairpin(5).energy
