class VariantResolver:

    def resolve(
        self,
        routine,
        definition,
        parameters
    ):

        if not routine.variants:
            return definition

        raise NotImplementedError(
            f"Routine '{routine.id}' variant resolution not implemented."
        )