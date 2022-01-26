from typeql_python.common.exception.typeql_exception import TypeQLException, INVALID_CASTING
from typeql_python.types.pattern import PatternT

#from typeql_python.pattern.conjunction import Conjunction
#from typeql_python.pattern.disjunction import Disjunction
#from typeql_python.pattern.negation import Negation
#from typeql_python.pattern.variable.bound_variable import BoundVariable


class IPattern(PatternT):
   
    def normalise(self):
        pass

    def patterns(self):
        pass

    def validate_bounded_by(self) -> None:
        pass

    def is_variable(self) -> bool:
        return False

    def is_conjunction(self) -> bool:
        return False

    def is_disjunction(self) -> bool:
        return False
   
    def is_conjuctable(self) -> bool:
        return False
   
    def is_negation(self) -> bool:
        return False

    def as_variable(self):
        raise TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, BoundVariable.__class__.__name__
        )

    def as_conjunction(self):
        raise TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, Conjunction.__class__.__name__
        )

    def as_disjuction(self):
        raise TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, Disjunction.__class__.__name__
        )

    def as_negation(self):
        raise TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, Negation.__class__.__name__
        )

    def as_conjuctable(self):
        raise TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, Negation.__class__.__name__
        )