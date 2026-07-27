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

        # Depois procura nos parâmetros dos requirements
        for requirement in self.requirements:

            for parameter in requirement.get("parameters", []):

                if parameter["parameter"] == parameter_id:
                    return parameter

        return None