class ConceptVariable(BoundVariable):

    def __init__(self, isConstraint, reference):
        self._isConstraint = isConstraint
        super().__init__(reference)
    
    def is_concept(self) -> bool:
        return True
    
    def as_concept(self):
        return self
    
    @property
    def constraints(self):
        empty_list = []
        if self._isConstraint != None:
            return list(self._isConstraint)
        else:
            return empty_list

    def iS(self):

    def __str__(self) -> str:
        if self._isConstraint == None
            return self._reference.__str__() + SPACE + self._isConstraint.__str__()

    def __eq__(self, other) -> bool:

    
    def __hash__(self):
        return hash((self._reference, self._isConstraint))
