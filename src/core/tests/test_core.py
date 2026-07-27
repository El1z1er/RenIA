from src.core.repositories.routine_library import RoutineLibrary

from src.core.resolvers.definition_resolver import DefinitionResolver
from src.core.resolvers.parameter_resolver import ParameterResolver

from src.core.validators.parameter_validator import ParameterValidator
from src.core.validators.validator import Validator


def test_routine_library():

    print("Testing RoutineLibrary...")

    library = RoutineLibrary()

    assert library.count() > 0
    assert library.exists("P9811")

    routine = library.get("P9811")

    assert routine.id == "P9811"

    print("✔ RoutineLibrary")


def test_definition_resolver():

    print("Testing DefinitionResolver...")

    library = RoutineLibrary()

    routine = library.get("P9811")

    resolver = DefinitionResolver()

    definition = resolver.resolve(
        routine,
        {}
    )

    assert definition is not None

    print("✔ DefinitionResolver")

    return definition


def test_definition_parameters(definition):

    print("Testing RoutineDefinition...")

    assert definition.get_parameter("X") is not None
    assert definition.get_parameter("Y") is not None
    assert definition.get_parameter("Z") is not None

    assert definition.get_parameter("S") is not None
    assert definition.get_parameter("T") is not None

    assert definition.get_parameter("INVALID") is None

    print("✔ RoutineDefinition")


def test_parameter_resolver(definition):

    print("Testing ParameterResolver...")

    resolver = ParameterResolver()

    parameter = resolver.resolve(
        definition,
        "X"
    )

    assert parameter is not None
    assert parameter.id == "X"
    assert parameter.type == "float"

    assert resolver.resolve(
        definition,
        "INVALID"
    ) is None

    print("✔ ParameterResolver")


def test_parameter_validator(definition):

    print("Testing ParameterValidator...")

    validator = ParameterValidator()

    errors = validator.validate(
        definition,
        {
            "X": 10.0,
            "S": 54
        }
    )

    assert errors == []

    errors = validator.validate(
        definition,
        {
            "X": 10.0,
            "INVALID": 123
        }
    )

    assert len(errors) == 1

    print("✔ ParameterValidator")


def test_validator():

    print("Testing Validator...")

    validator = Validator()

    valid, errors = validator.validate(
        "P9811",
        {
            "X": 100.0
        }
    )

    assert valid
    assert errors == []

    valid, errors = validator.validate(
        "P9811",
        {
            "INVALID": 100
        }
    )

    assert not valid
    assert len(errors) > 0

    print("✔ Validator")


if __name__ == "__main__":

    test_routine_library()

    definition = test_definition_resolver()

    test_definition_parameters(definition)

    test_parameter_resolver(definition)

    test_parameter_validator(definition)

    test_validator()

    print()
    print("===================================")
    print(" All core tests passed successfully")
    print("===================================")