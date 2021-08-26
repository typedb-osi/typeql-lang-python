from abc import ABC, abstractmethod
from common.exception.typeql_exception import TypeQLException, INVALID_CASTING
from pattern.conjunction import Conjunction
from pattern.disjunction import Disjunction
from pattern.negation import Negation
from pattern.variable.bound_variable import BoundVariable
class IPattern(ABC):
    @abstractmethod
    def normalise(self):
        pass

    @abstractmethod
    def patterns(self):
        pass

    @abstractmethod
    def validate_bounded_by(self):
        pass

    @abstractmethod
    def is_variable(self) -> bool:
        return False

    @abstractmethod
    def is_conjunction(self) -> bool:
        return False

    @abstractmethod
    def is_disjunction(self) -> bool:
        return False

    @abstractmethod
    def is_conjuctable(self) -> bool:
        return False

    @abstractmethod
    def is_negation(self) -> bool:
        return False

    @abstractmethod
    def as_variable(self):
        raise TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, BoundVariable.__class__.__name__
        )

    @abstractmethod
    def as_conjunction(self):
        raise TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, Conjunction.__class__.__name__
        )

    @abstractmethod
    def as_disjuction(self):
        raise TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, Disjunction.__class__.__name__
        )

    @abstractmethod
    def as_negation(self):
        raise TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, Negation.__class__.__name__
        )

    @abstractmethod
    def as_conjuctable(self):
        raise TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, Negation.__class__.__name__
        )
