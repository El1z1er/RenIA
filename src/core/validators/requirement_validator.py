class RequirementValidator:

    def validate(
        self,
        definition,
        parameters
    ):

        errors = []

        for requirement in definition.requirements:

            rule = requirement["rule"]

            if rule == "required":

                errors.extend(
                    self._validate_required(
                        requirement,
                        parameters
                    )
                )

            elif rule == "all":

                errors.extend(
                    self._validate_all(
                        requirement,
                        parameters
                    )
                )

            elif rule == "one_or_more":

                errors.extend(
                    self._validate_one_or_more(
                        requirement,
                        parameters
                    )
                )

            elif rule == "one_of":

                errors.extend(
                    self._validate_one_of(
                        requirement,
                        parameters
                    )
                )

        return errors

    # --------------------------------------------------

    def _validate_required(
        self,
        requirement,
        parameters
    ):

        errors = []

        for parameter in requirement["parameters"]:

            if parameter not in parameters:

                errors.append(
                    f"Required parameter '{parameter}' is missing."
                )

        return errors

    # --------------------------------------------------

    def _validate_all(
        self,
        requirement,
        parameters
    ):

        errors = []

        for parameter in requirement["parameters"]:

            if parameter not in parameters:

                errors.append(
                    f"Required parameter '{parameter}' is missing."
                )

        return errors

    # --------------------------------------------------

    def _validate_one_or_more(
        self,
        requirement,
        parameters
    ):

        errors = []

        required = requirement["parameters"]

        if not any(
            parameter in parameters
            for parameter in required
        ):

            errors.append(
                "At least one of the following parameters is required: "
                + ", ".join(required)
            )

        return errors

    # --------------------------------------------------

    def _validate_one_of(
        self,
        requirement,
        parameters
    ):

        errors = []

        required = requirement["parameters"]

        count = sum(
            parameter in parameters
            for parameter in required
        )

        if count != 1:

            errors.append(
                "Exactly one of the following parameters is required: "
                + ", ".join(required)
            )

        return errors