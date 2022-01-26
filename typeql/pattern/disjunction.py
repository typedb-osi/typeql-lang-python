

from typing import List, Pattern
from typeql.common.typeql_token import TypeQLToken 

class Disjunction(IPattern):

    patterns : List
    hash: int
    #normalised

    def __init__(self, patterns) -> None:
        if patterns == None:
            raise
        self.patterns 
        self._hash 

    @property
    def patterns(self):
        return self._patterns

    def validate_is_bounded_by(self, bounds):
        for pattern in self._patterns:
            pattern.validate_is_bounded_by(bounds)

    
    def normalise(self):
        if normalised == None

    def is_disjunction(self) -> bool:
        return True

    def as_disjunction(self) -> bool:
        return self


    #def __str__(self):
    

    #def __eq__(self):
