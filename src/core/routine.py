class Routine:

    def __init__(self, data):

        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]

        self.requirements = data.get("requirements", [])
        self.optional_parameters = data.get("optional_parameters", [])
        self.variants = data.get("variants", [])