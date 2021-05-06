from abc import ABC, abstractmethod


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
        raise  TypeQLException.of(INVALID_CASTING,
                                self.__class__.__name__, 
                                BoundVariable.__class__.__name__)
    @abstractmethod
    def as_conjunction(self):
        raise  TypeQLException.of(INVALID_CASTING,
                                self.__class__.__name__, 
                                Conjunction.__class__.__name__)

    @abstractmethod
    def as_disjuction(self):
        raise  TypeQLException.of(INVALID_CASTING,
                                self.__class__.__name__, 
                                Disjunction.__class__.__name__)

    @abstractmethod
    def as_negation(self):
        raise  GraqlException.of(INVALID_CASTING,
                                self.__class__.__name__, 
                                Negation.__class__.__name__)

    @abstractmethod
    def as_conjuctable(self):
        raise  GraqlException.of(INVALID_CASTING,
                                self.__class__.__name__, 
                                Negation.__class__.__name__)