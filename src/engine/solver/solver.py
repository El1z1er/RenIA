from .resolvers.routine_resolver import RoutineResolver
from src.engine.solution.solution import Solution


class Solver:

    def __init__(self, engine):

        self.engine = engine
        self.routine_resolver = RoutineResolver(engine)

    def solve(
        self,
        objective
    ):

        routine = self.routine_resolver.resolve(
            objective
        )

        solution = Solution()

        solution.objective = objective

        solution.routine = routine

        return solution