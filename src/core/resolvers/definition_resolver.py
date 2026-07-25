from .option_resolver import OptionResolver
from .variant_resolver import VariantResolver


class DefinitionResolver:

    def __init__(self):

        self.option_resolver = OptionResolver()
        self.variant_resolver = VariantResolver()

    def resolve(
        self,
        routine,
        parameters,
        option_name=None
    ):

        definition = self.option_resolver.resolve(
            routine,
            option_name
        )

        definition = self.variant_resolver.resolve(
            routine,
            definition,
            parameters
        )

        return definition