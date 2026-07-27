class ParameterValidator:

    def validate(
        self,
        definition,
        parameters
    ):

        errors = []

        for parameter in parameters:

            if definition.get_parameter(parameter) is None:

                errors.append(
                    f"Unknown parameter '{parameter}'."
                )

        return errors