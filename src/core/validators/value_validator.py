from ..resolvers.parameter_resolver import ParameterResolver


class ValueValidator:

    def __init__(self):

        self.parameter_resolver = ParameterResolver()

    def validate(
        self,
        definition,
        parameters
    ):

        errors = []

        for parameter_id, value in parameters.items():

            parameter = self.parameter_resolver.resolve(
                definition,
                parameter_id
            )

            if parameter is None:
                continue

            errors.extend(
                self._validate_parameter(
                    parameter,
                    value
                )
            )

        return errors

    # --------------------------------------------------

    def _validate_parameter(
        self,
        parameter,
        value
    ):

        errors = []

        # --------------------------------------------------
        # Type
        # --------------------------------------------------

        if parameter.type == "integer":

            if not isinstance(value, int):

                errors.append(
                    f"Parameter '{parameter.id}' must be an integer."
                )

                return errors

        elif parameter.type == "float":

            if not isinstance(value, (int, float)):

                errors.append(
                    f"Parameter '{parameter.id}' must be a float."
                )

                return errors

        # --------------------------------------------------
        # Minimum
        # --------------------------------------------------

        if parameter.minimum is not None:

            if value < parameter.minimum:

                errors.append(
                    f"Parameter '{parameter.id}' must be greater than or equal to {parameter.minimum}."
                )

        # --------------------------------------------------
        # Maximum
        # --------------------------------------------------

        if parameter.maximum is not None:

            if value > parameter.maximum:

                errors.append(
                    f"Parameter '{parameter.id}' must be less than or equal to {parameter.maximum}."
                )

        # --------------------------------------------------
        # Allowed values
        # --------------------------------------------------

        if parameter.allowed_values is not None:

            if value not in parameter.allowed_values:

                errors.append(
                    f"Parameter '{parameter.id}' must be one of: {parameter.allowed_values}."
                )

        # --------------------------------------------------
        # Allowed ranges
        # --------------------------------------------------

        if parameter.allowed_ranges is not None:

            if not any(
                lower <= value <= upper
                for lower, upper in parameter.allowed_ranges
            ):

                errors.append(
                    f"Parameter '{parameter.id}' must be within one of the allowed ranges: {parameter.allowed_ranges}."
                )

        return errors
