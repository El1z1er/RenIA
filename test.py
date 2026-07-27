from src.engine.engine import Engine
from src.engine.request.request import Request


request = Request(
    "Quero medir um furo de 20 mm."
)

engine = Engine()

solution = engine.execute(
    request
)

print(solution.objective.action)
print(solution.objective.target)
print(solution.objective.properties)
print(solution.routine.id)