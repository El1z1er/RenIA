from src.core.repositories.routine_library import RoutineLibrary
from src.core.matchers.routine_matcher import RoutineMatcher


class Core:

    def __init__(self):

        self.routine_library = RoutineLibrary()
        self.routine_matcher = RoutineMatcher(
            self.routine_library
        )

    def find_routine(
        self,
        objective
    ):

        return self.routine_matcher.match(
            objective
        )