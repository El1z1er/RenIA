from core.repositories.routine_library import RoutineLibrary

library = RoutineLibrary()

library.load()

print(library.routines)