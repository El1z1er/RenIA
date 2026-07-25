class PermissionValidator:

    def validate(
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