from typeql.pattern.pattern import IPattern
from typeql.common.exception.typeql_exception import TypeQLException, INVALID_CASTING

class IConjunctable(IPattern):

    def is_variable(self) -> bool:
        return False

    def is_negation(self) -> bool:
        return False
    
    def is_conjuctable(self) -> bool:
        return True


    def as_variable(self):
        return  TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, BoundVariable.__class__.__name__
        )

    def as_negation(self):
        return  TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, Negation.__class__.__name__
        )

    def as_conjunctable(self):
        return self
