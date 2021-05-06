
class Negation(Conjunctable):

    def __init__(self, pattern: list, normalised):
        self._normalised = normalised

        if pattern == None:
            raise TypeError
        elif pattern.is_negation:
            raise  GraqlException.of(REDUNDANT_NESTED_NEGATION)
        else: 
            self._pattern = pattern
    
    @property
    def pattern(self):
        return self._pattern
    

    def patterns(self):
    
    def validate_bounded_by(self, bounds):
        if self._pattern.is_negation():
            raise
        else:
            pattern.validate_bounded_by(bounds)    

    @property
    def normalise(self):
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
        negation = NOT + SPACE
        pattern = self._pattern.to_string()

        if self._pattern.is_conjunction():
            negation += pattern
        else:
            negation += CURLY_OPEN + SPACE
            negation += pattern
            negation += SEMICOLN + SPACE + CURLY_CLOSE
        return negation
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Negation):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self._pattern == other.pattern
    
    def __hash__(self):
        return hash(self._pattern)

