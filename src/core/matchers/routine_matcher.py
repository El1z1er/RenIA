class RoutineMatcher:

    def __init__(
        self,
        routine_library
    ):
        self.routine_library = routine_library

    def match(
        self,
        objective
    ):

        routines = self.routine_library.list()

        for routine in routines:

            if self._match_objective(
                objective,
                routine
            ):

                return routine

        return None