from .routine_library import RoutineLibrary
from .parameter_library import ParameterLibrary


class Validator:

    def __init__(self):

        self.routines = RoutineLibrary()
        self.parameters = ParameterLibrary()

    def validate(self, routine_id, parameters):

        errors = []

        routine = self.routines.get(routine_id)

        errors.extend(
            self._validate_routine(routine, routine_id)
        )

        errors.extend(
            self._validate_parameters_exist(parameters)
        )

        if routine:

            definition = routine.resolve(parameters)

            errors.extend(
                self._validate_allowed_parameters(
                    definition,
                    parameters,
                    routine_id
                )
            )

            errors.extend(
                self._validate_required_parameters(
                    definition,
                    parameters
                )
            )

        return (
            len(errors) == 0,
            errors
        )

    # --------------------------------------------------

    def _validate_routine(self, routine, routine_id):

        if routine is None:
            return [f"Routine '{routine_id}' not found."]

        return []

    # --------------------------------------------------

    def _validate_parameters_exist(self, parameters):

        errors = []

        for parameter in parameters:

            if not self.parameters.exists(parameter):
                errors.append(
                    f"Unknown parameter '{parameter}'."
                )

        return errors

    # --------------------------------------------------

    def _validate_allowed_parameters(
        self,
        definition,
        parameters,
        routine_id
    ):

        errors = []

        allowed = set()

        for requirement in definition.requirements:

            allowed.update(
                requirement["parameters"]
            )

        for optional in definition.optional_parameters:

            allowed.add(
                optional["parameter"]
            )

        for parameter in parameters:

            if parameter not in allowed:

                errors.append(
                    f"Parameter '{parameter}' is not allowed for routine '{routine_id}'."
                )

        return errors

    # --------------------------------------------------

    def _validate_required_parameters(
        self,
        definition,
        parameters
    ):

        errors = []

        for requirement in definition.requirements:

            rule = requirement["rule"]

            if rule == "required":

                errors.extend(
                    self._validate_required(
                        requirement,
                        parameters
                    )
                )

            elif rule == "all":

                errors.extend(
                    self._validate_all(
                        requirement,
                        parameters
                    )
                )

            elif rule == "one_or_more":

                errors.extend(
                    self._validate_one_or_more(
                        requirement,
                        parameters
                    )
                )

            elif rule == "one_of":

                errors.extend(
                    self._validate_one_of(
                        requirement,
                        parameters
                    )
                )

        return errors

    # --------------------------------------------------

    def _validate_required(
        self,
        requirement,
        parameters
    ):

        errors = []

        for parameter in requirement["parameters"]:

            if parameter not in parameters:

                errors.append(
                    f"Required parameter '{parameter}' is missing."
                )

        return errors

    # --------------------------------------------------

    def _validate_all(
        self,
        requirement,
        parameters
    ):

        errors = []

        for parameter in requirement["parameters"]:

            if parameter not in parameters:

                errors.append(
                    f"Required parameter '{parameter}' is missing."
                )

        return errors

    # --------------------------------------------------

    def _validate_one_or_more(
        self,
        requirement,
        parameters
    ):

        errors = []

        required = requirement["parameters"]

        if not any(
            parameter in parameters
            for parameter in required
        ):

            errors.append(
                "At least one of the following parameters is required: "
                + ", ".join(required)
            )

        return errors

    # --------------------------------------------------

    def _validate_one_of(
        self,
        requirement,
        parameters
    ):

        errors = []

        required = requirement["parameters"]

        count = sum(
            parameter in parameters
            for parameter in required
        )

        if count != 1:

            errors.append(
                "Exactly one of the following parameters is required: "
                + ", ".join(required)
            )

        return errors