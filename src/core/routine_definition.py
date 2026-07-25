class RoutineDefinition:

    def __init__(
        self,
        requirements=None,
        optional_parameters=None
    ):

        self.requirements = requirements or []
        self.optional_parameters = optional_parameters or []