class ConceptConstraint(Constraint):

    def is_concept(self) -> bool:
        return True
    
    def as_concept(self):
        return self
    
    def variables(self):
        return None
    
    def is_Is(self):
        return False
    
    def as_Is(self):
        raise # TODO

class Is(ConceptConstraint):

    def __init__(self, variable):
        self._variable = variable.to_concept