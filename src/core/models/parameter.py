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