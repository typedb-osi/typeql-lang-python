
class ConceptConstraint(Constraint):

    def is_concept(self) -> bool:
        return True

    def as_concept(self):
        return self

    def variables(self):
        return None

    def is_is(self):
        return False

    def as_is(self):
        raise TypeQLException.of(
            INVALID_CASTING, 
            self.__class__.__name__, 
            ConceptConstraint.__class__.__name__
        )
    #def __str__(self) -> str:
    #def __eq__(self) -> bool:
    #def __hash__(self):  


class Is(ConceptConstraint):
    
    @dispatch(UnboundVariable)
    def __init__(self, variable):
        self._variable = variable.to_concept()

    @dispatch(ConceptVariable)
    def __init__(self, variable):
        if variable == None:
            raise TypeError
        self._variable = variable
        
    @property
    def variable(self) -> ConceptVariable :
        return self._variable

    def variables(self) -> List[ConceptVariable]:
        #TODO

    def is_is(self):
        return True
    
    def as_is(self):
        return self
    
    #def __str__(self):
    #def __eq__(self):
    #def __hash__(self):  