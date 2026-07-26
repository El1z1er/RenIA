from ..repositories.parameter_library import ParameterLibrary


class ParameterResolver:

    def __init__(self):

        self.parameters = ParameterLibrary()

    def resolve(
        self,
        definition,
        parameter_id
    ):

        parameter = self.parameters.get(parameter_id)

        if parameter is None:
            return None

        parameter = parameter.copy()

        override = definition.get_parameter(
            parameter_id
        )

        if override:

            for key, value in override.items():

                if key == "parameter":
                    continue

                setattr(
                    parameter,
                    key,
                    value
                )

        return parameter