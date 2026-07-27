from .objective import Objective


class ObjectiveBuilder:

    ACTIONS = {
    "medir": "measure",
}

    TARGETS = {
    "furo": "hole",
    "eixo": "shaft",
    "plano": "plane",
    "rasgo": "slot",
    "ressalto": "boss",
}

    def build(self, request):

        objective = Objective()

        objective.request = request
        objective.action = self._extract_action(request)
        objective.target = self._extract_target(request)
        objective.properties = self._extract_properties(request)

        return objective

    def _extract_action(self, request):

        message = request.message.lower()

        for key, value in self.ACTIONS.items():

            if key in message:
                return value

        return None

    def _extract_target(self, request):

        message = request.message.lower()

        for key, value in self.TARGETS.items():

            if key in message:
                return value

        return None

    def _extract_properties(
        self,
        request
    ):

        properties = {}

        message = request.message.lower()

        self._extract_hole_properties(
            message,
            properties
        )

        self._extract_shaft_properties(
            message,
            properties
        )

        return properties

    def _extract_hole_properties(
        self,
        message,
        properties
    ):

        if "furo" not in message:
            return

        words = message.split()

        for word in words:

            try:

                properties["diameter"] = float(
                word.replace(",", ".")
                )

                return

            except ValueError:
                continue


    def _extract_shaft_properties(
        self,
        message,
        properties
    ):

        if "eixo" not in message:
            return

        words = message.split()

        for word in words:

            try:

                properties["diameter"] = float(
                    word.replace(",", ".")
                )

                return

            except ValueError:
                continue