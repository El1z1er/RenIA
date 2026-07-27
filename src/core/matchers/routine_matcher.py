from src.core.entities.routine_match import RoutineMatch


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

        for routine in self.routine_library.list():

            if self._match_routine(
                objective,
                routine
            ):

                routine_match = RoutineMatch()

                routine_match.routine = routine

                return routine_match

            for option in routine.options:

                if self._match_option(
                    objective,
                    option
                ):

                    routine_match = RoutineMatch()

                    routine_match.routine = routine

                    routine_match.option = option

                    return routine_match

        return None

    def _match_routine(
        self,
        objective,
        routine
    ):

        for rule in routine.match:

            if (
                rule["action"] == objective.action
                and
                rule["target"] == objective.target
            ):

                return True

        return False

    def _match_option(
        self,
        objective,
        option
    ):

        for rule in option.match:

            if (
                rule["action"] == objective.action
                and
                rule["target"] == objective.target
            ):

                return True

        return False