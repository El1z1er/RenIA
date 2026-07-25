class RoutineValidator:

    def validate(
        self,
        routine,
        routine_id
    ):

        if routine is None:
            return [
                f"Routine '{routine_id}' not found."
            ]

        return []