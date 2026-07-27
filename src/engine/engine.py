from src.engine.objective.objective_builder import ObjectiveBuilder
from src.engine.solver.solver import Solver
from src.engine.generator.generator import Generator
from src.core.core import Core


class Engine:

    def __init__(self):

        self.core = Core()

        self.objective_builder = ObjectiveBuilder()
        self.solver = Solver(self)
        self.generator = Generator()

    def execute(
        self,
        request
    ):

        objective = self.objective_builder.build(
            request
        )

        solution = self.solver.solve(
            objective
        )

        return solution

    def find_routine(
        self,
        objective
    ):

        return self.core.find_routine(
            objective
        )