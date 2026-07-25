from pathlib import Path
import json

from .parameter import Parameter


class ParameterLibrary:

    def __init__(self):
        self.parameters = {}
        self._load_parameters()

    def _load_parameters(self):
        parameters_path = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "parameters"
        )

        for file in parameters_path.glob("*.json"):
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            parameter = Parameter(data)

            if parameter.id in self.parameters:
                raise ValueError(f"Duplicate parameter ID: {parameter.id}")

            self.parameters[parameter.id] = parameter

    def get(self, parameter_id):
        return self.parameters.get(parameter_id)

    def exists(self, parameter_id):
        return parameter_id in self.parameters

    def list(self):
        return list(self.parameters.values())

    def count(self):
        return len(self.parameters)

    def ids(self):
        return sorted(self.parameters.keys())