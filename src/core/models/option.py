class Option:

    def __init__(self, data):

        self.name = data["name"]

        self.match = data.get("match", [])

        self.requirements = data.get(
            "requirements",
            []
        )