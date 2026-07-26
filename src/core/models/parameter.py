class Parameter:

    def __init__(self, data):

        self.id = data["id"]
        self.name = data["name"]
        self.description = data.get("description")
        self.type = data.get("type")

        self.default = data.get("default")

        self.minimum = data.get("minimum")
        self.maximum = data.get("maximum")

        self.allowed_values = data.get("allowed_values")
        self.allowed_ranges = data.get("allowed_ranges")

    def copy(self):

        parameter = Parameter(
            {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "type": self.type,
                "default": self.default,
                "minimum": self.minimum,
                "maximum": self.maximum,
                "allowed_values": self.allowed_values,
                "allowed_ranges": self.allowed_ranges
            }
        )

        return parameter