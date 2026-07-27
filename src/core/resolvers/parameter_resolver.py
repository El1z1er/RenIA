from ..models.parameter import Parameter


class ParameterResolver:

    def resolve(
        self,
        definition,
        parameter_id
    ):

        parameter = definition.get_parameter(
            parameter_id
        )

        if parameter is None:
            return None

        return Parameter(parameter)