from typing import Set
from typeql.pattern.conjuctable import IConjunctable
from typeql.common.exception.typeql_exception import ILLEGAL_STATE, TypeQLException,REDUNDANT_NESTED_NEGATION
from typeql.common.typeql_token import TypeQLToken

class Negation(IConjunctable):

    def __init__(self, pattern):


        self._normalised : IConjunctable

        if pattern == None:
            raise TypeError
        elif pattern.is_negation:
            raise  TypeQLException.of(REDUNDANT_NESTED_NEGATION)
        else: 
            self._pattern = pattern
    

    @property
    def pattern(self):
        return self._pattern
    
    @property
    def patterns(self):
        list(self._pattern)

    
    def validate_bounded_by(self, bounds: Set[UnboundVariable]) -> None:
        if self._pattern.is_negation():
            raise TypeQLException.of(ILLEGAL_STATE)
        else:
            self.pattern.validate_bounded_by(bounds)  

    @property
    def normalise(self)-> IConjunctable:
        return self._normalised
    
    @property.setter
    def normalise(self):
        if self._normalised == None:
            if self._pattern.is_negation():
                raise # TODO
            elif self._pattern.is_variable():
                normalised = 
            else :
                if self._pattern.is_disjunction():
                    self._normalised = self._pattern.as_conjunction.normalise()
                else: 
                    self._normalised = self._pattern.as_disjuction.normalise()


    def is_negation(self) -> bool:
        return True
    
    def as_negation(self):
        return self
    
    def __str__(self):
        negation = TypeQLToken.Operator.NOT + TypeQLToken.Char.SPACE
        pattern = self._pattern.__str__()

        if self._pattern.is_conjunction():
            negation += pattern
        else:
            negation += TypeQLToken.Char.CURLY_OPEN + TypeQLToken.Char.SPACE
            negation += pattern
            negation += TypeQLToken.Char.SEMICOLON + TypeQLToken.Char.SPACE + TypeQLToken.Char.CURLY_CLOSE
        return negation
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Negation):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self._pattern == other.pattern
    
    def __hash__(self):
        return hash(self._pattern)