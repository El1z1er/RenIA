class Parameter:

    def __init__(self, data):

        self.id = data.get("id", data.get("parameter"))

        self.name = data.get("name")
        self.attribute = data.get("attribute")
        self.description = data.get("description")

        self.type = data.get("type")

        self.default = data.get("default")

        self.minimum = data.get("minimum")
        self.maximum = data.get("maximum")

        self.allowed_values = data.get("allowed_values")
        self.allowed_ranges = data.get("allowed_ranges")