from .routine_library import RoutineLibrary
from .parameter_library import ParameterLibrary


class Validator:

    def __init__(self):
        self.routines = RoutineLibrary()
        self.parameters = ParameterLibrary()

    def validate(self, routine_id, parameters):

        if not self.routines.exists(routine_id):
            return False, f"Routine '{routine_id}' not found."

        return True, "Validation successful."