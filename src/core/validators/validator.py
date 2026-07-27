from ..repositories.routine_library import RoutineLibrary

from ..resolvers.definition_resolver import DefinitionResolver

from .routine_validator import RoutineValidator
from .parameter_validator import ParameterValidator
from .permission_validator import PermissionValidator
from .requirement_validator import RequirementValidator
from .value_validator import ValueValidator


class Validator:

    def __init__(self):

        self.routines = RoutineLibrary()

        self.definition_resolver = DefinitionResolver()

        self.routine_validator = RoutineValidator()
        self.parameter_validator = ParameterValidator()
        self.permission_validator = PermissionValidator()
        self.requirement_validator = RequirementValidator()
        self.value_validator = ValueValidator()

    def validate(
        self,
        routine_id,
        parameters,
        option_name=None
    ):

        errors = []

        routine = self.routines.get(routine_id)

        errors.extend(
            self.routine_validator.validate(
                routine,
                routine_id
            )
        )

        if errors:
            return False, errors

        definition = self.definition_resolver.resolve(
            routine,
            parameters,
            option_name
        )

        errors.extend(
            self.parameter_validator.validate(
                definition,
                parameters
            )
        )

        errors.extend(
            self.permission_validator.validate(
                definition,
                parameters,
                routine_id
            )
        )

        errors.extend(
            self.requirement_validator.validate(
                definition,
                parameters
            )
        )

        errors.extend(
            self.value_validator.validate(
                definition,
                parameters
            )
        )

        return (
            len(errors) == 0,
            errors
        )