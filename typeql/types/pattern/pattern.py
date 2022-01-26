import abc

from common.exception.typeql_exception import TypeQLException, INVALID_CASTING
from pattern.conjunction import Conjunction
from pattern.disjunction import Disjunction
from pattern.negation import Negation
from pattern.variable.bound_variable import BoundVariable


class PatternT(abc.ABC):

    @abc.abstractmethod
    def normalise(self):
        ...

    @abc.abstractmethod
    def patterns(self):
        ...

    @abc.abstractmethod
    def validate_bounded_by(self):
        ...

    @abc.abstractmethod
    def is_variable(self) -> bool:
        ...

    @abc.abstractmethod
    def is_conjunction(self) -> bool:
        ...
 
    @abc.abstractmethod
    def is_disjunction(self) -> bool:
        ...

    @abc.abstractmethod
    def is_conjuctable(self) -> bool:
        ...
 
    @abc.abstractmethod
    def is_negation(self) -> bool:
        ...

    @abc.abstractmethod
    def as_variable(self):
        ...

    @abc.abstractmethod
    def as_conjunction(self):
        ...
    
    @abc.abstractmethod
    def as_disjuction(self):
        ...

    @abc.abstractmethod
    def as_negation(self):
        ...

    @abc.abstractmethod
    def as_conjuctable(self):
        ...
