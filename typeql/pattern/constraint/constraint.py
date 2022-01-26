
class Constraint(ConstraintT):

    def __init__(self):
        pass

    def variables(self):
        return False

    def is_concept(self) -> bool:
        return False

    def is_type(self) -> bool:
        return False

    def is_thing(self) -> bool:
        return False

    def as_concept(self):
        raise TypeQLException.of(
            INVALID_CASTING, 
            self.__class__.__name__, 
            ConceptConstraint.__class__.__name__
        )

    def as_type(self):
        raise TypeQLException.of(
            INVALID_CASTING, 
            self.__class__.__name__, 
            TypeConstraint.__class__.__name__
        )

    def as_thing(self):
        raise TypeQLException.of(
            INVALID_CASTING, 
            self.__class__.__name__, 
            ThingConstraint.__class__.__name__
        )

    def __str__(self):
        pass