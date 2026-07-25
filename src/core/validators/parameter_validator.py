class ParameterValidator:

    def __init__(self, parameter_library):

        self.parameters = parameter_library

    def validate(
        self,
        parameters
    ):

        errors = []

        for parameter in parameters:

            if not self.parameters.exists(parameter):

                errors.append(
                    f"Unknown parameter '{parameter}'."
                )

        return errors