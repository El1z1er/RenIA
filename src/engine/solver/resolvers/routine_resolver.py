
class RoutineResolver:

    def __init__(self, engine):

        self.engine = engine

    def resolve(
        self,
        objective
    ):
        
        return self.engine.find_routine(
            objective
        )