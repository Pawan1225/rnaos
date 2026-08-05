from enterprise.validation import (
    ValidationCategory,
    ValidationRegistry,
    ValidationResult,
    ValidationSeverity,
    ValidationStatus,
)


class ValidatorOne:
    @property
    def name(self) -> str:
        return "RNA"

    def validate(self) -> ValidationResult:
        return ValidationResult(
            name=self.name,
            status=ValidationStatus.PASSED,
            category=ValidationCategory.SYSTEM,
            severity=ValidationSeverity.LOW,
        )


class ValidatorTwo:
    @property
    def name(self) -> str:
        return "Cloud"

    def validate(self) -> ValidationResult:
        return ValidationResult(
            name=self.name,
            status=ValidationStatus.PASSED,
            category=ValidationCategory.SYSTEM,
            severity=ValidationSeverity.LOW,
        )


def test_register():
    registry = ValidationRegistry()

    registry.register(ValidatorOne())

    assert registry.count() == 1


def test_lookup():
    registry = ValidationRegistry()

    validator = ValidatorOne()

    registry.register(validator)

    assert registry.get("RNA") is validator


def test_exists():
    registry = ValidationRegistry()

    registry.register(ValidatorTwo())

    assert registry.exists("Cloud")


def test_remove():
    registry = ValidationRegistry()

    registry.register(ValidatorTwo())

    registry.remove("Cloud")

    assert registry.count() == 0


def test_clear():
    registry = ValidationRegistry()

    registry.register(ValidatorOne())
    registry.register(ValidatorTwo())

    registry.clear()

    assert registry.count() == 0


def test_list():
    registry = ValidationRegistry()

    registry.register(ValidatorTwo())
    registry.register(ValidatorOne())

    assert registry.list_validators() == [
        "Cloud",
        "RNA",
    ]


def test_items():
    registry = ValidationRegistry()

    validator = ValidatorOne()

    registry.register(validator)

    items = registry.items()

    assert len(items) == 1
    assert items[0] is validator
    assert items[0].name == "RNA"
