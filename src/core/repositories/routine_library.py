from pathlib import Path
import json

from ..models.routine import Routine


class RoutineLibrary:
    """Loads and provides access to all Renishaw routines."""

    def __init__(self):

        self.routines = {}
        self._load_routines()

    def _load_routines(self):

        routines_path = (
            Path(__file__).resolve().parents[3]
            / "data"
            / "routines"
        )

        for file in routines_path.glob("*.json"):

            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            routine = Routine(data)

            if routine.id in self.routines:
                raise ValueError(
                    f"Duplicate routine ID: {routine.id}"
                )

            self.routines[routine.id] = routine

    def get(self, routine_id):

        return self.routines.get(routine_id)

    def exists(self, routine_id):

        return routine_id in self.routines

    def list(self):

        return list(self.routines.values())

    def count(self):

        return len(self.routines)

    def ids(self):

        return sorted(self.routines.keys())