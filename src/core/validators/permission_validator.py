class PermissionValidator:

    def validate(
        self,
        definition,
        parameters,
        routine_id
    ):

        errors = []

        allowed = set()

        # Parâmetros definidos nos requirements
        for requirement in definition.requirements:

            for parameter in requirement.get("parameters", []):

                allowed.add(
                    parameter["parameter"]
                )

        # Parâmetros opcionais
        for optional in definition.optional_parameters:

            allowed.add(
                optional["parameter"]
            )

        # Verifica se os parâmetros informados são permitidos
        for parameter in parameters:

            if parameter not in allowed:

                errors.append(
                    f"Parameter '{parameter}' is not allowed for routine '{routine_id}'."
                )

        return errors