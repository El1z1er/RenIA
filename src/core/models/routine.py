from .option import Option

class Routine:

    def __init__(self, data):

        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]

        self.match = data.get("match", [])

        self.requirements = data.get("requirements", [])
        self.optional_parameters = data.get("optional_parameters", [])

        self.options = []

        for option in data.get("options", []):

            self.options.append(
                Option(option)
            )
            
        self.variants = data.get("variants", [])