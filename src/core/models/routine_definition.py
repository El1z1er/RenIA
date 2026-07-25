class RoutineDefinition:

    def __init__(
        self,
        requirements=None,
        optional_parameters=None
    ):

        self.requirements = requirements or []
        self.optional_parameters = optional_parameters or []

    def get_parameter(self, parameter_id):

        # Primeiro procura nos opcionais
        for parameter in self.optional_parameters:

            if parameter["parameter"] == parameter_id:
                return parameter

        # Depois procura overrides dos obrigatórios
        for requirement in self.requirements:

            overrides = requirement.get(
                "overrides",
                {}
            )

            if parameter_id in overrides:

                parameter = {
                    "parameter": parameter_id
                }

                parameter.update(
                    overrides[parameter_id]
                )

                return parameter

        return {
            "parameter": parameter_id
        }