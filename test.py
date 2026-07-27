from src.core.core import Core


class Objective:

    action = "measure"
    target = "bore"


core = Core()

routine_match = core.routine_matcher.match(
    Objective()
)

print(routine_match.routine.id)
print(routine_match.option.name)