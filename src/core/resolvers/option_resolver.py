from ..models.routine_definition import RoutineDefinition


class OptionResolver:

    def resolve(
        self,
        routine,
        option_name=None
    ):

        if not routine.options:

            return RoutineDefinition(
                requirements=routine.requirements,
                optional_parameters=routine.optional_parameters
            )

        if option_name is None:

            raise ValueError(
                f"Routine '{routine.id}' requires an option."
            )

        option = self._find_option(
            routine,
            option_name
        )

        return RoutineDefinition(
            requirements=option["requirements"],
            optional_parameters=option.get(
                "optional_parameters",
                routine.optional_parameters
            )
        )

    def _find_option(
        self,
        routine,
        option_name
    ):

        for option in routine.options:

            if option["name"] == option_name:
                return option

        raise ValueError(
            f"Unknown option '{option_name}' for routine '{routine.id}'."
        )