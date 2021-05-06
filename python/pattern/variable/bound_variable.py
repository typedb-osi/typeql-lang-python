
class BoundVariable(Variable, Conjunctable):

    def __init__(self, reference):
        super().__init__(reference)
    
    def validate_bounded_by(self, bounds):

    def is_bound(self) -> bool:
        return True
    
    def as_bound(self) -> BoundVariable: 
        return self
    
    def as_concept(self):
        raise  GraqlException.of(INVALID_CASTING,
                                self.__class__.__name__, 
                                ConceptVariable.__class__.__name__)

    def as_type(self):
        raise  GraqlException.of(INVALID_CASTING,
                                self.__class__.__name__, 
                                TypeVariable.__class__.__name__)
    
    def as_thing(self):
        raise  GraqlException.of(INVALID_CASTING,
                                self.__class__.__name__, 
                                ThingVariable.__class__.__name__)
    @property
    def normalise(self) -> BoundVariable:
        return self
    
    def is_variable(self) -> bool:
        return True
    
    def as_variable(self) -> BoundVariable:
        return self
    
    def patterns(self):
        array = []
        # hope it's work
        return array.append(list(self))