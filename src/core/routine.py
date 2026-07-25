from .routine_definition import RoutineDefinition

class Routine:

    def __init__(self, data):

        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]

        self.requirements = data.get("requirements", [])
        self.optional_parameters = data.get("optional_parameters", [])
        self.variants = data.get("variants", [])

    @property
    def has_variants(self):

        return len(self.variants) > 0

    def resolve(self, parameters):

        if not self.has_variants:
            return self._default_definition()

        return self._resolve_variant(parameters)

    def _default_definition(self):

        return RoutineDefinition(
            requirements=self.requirements,
            optional_parameters=self.optional_parameters
        )

    def _resolve_variant(self, parameters):

        raise NotImplementedError(
            f"Routine '{self.id}' variant resolution not implemented."
        )