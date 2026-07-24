class Routine:

    def __init__(self, data):

        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.required = data["required"]
        self.optional = data["optional"]