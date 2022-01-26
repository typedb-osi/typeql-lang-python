

class BoundVariable():

    def __init__(self, reference):
        self._reference = reference
    
    def is_bound(self) -> bool:
        return True
    
    def as_bound(self) -> bool:
        return self
    
    def to_unbound(self) -> UnboundVariable:
        return UnboundVariable(reference)
    
    def as_concept(self) -> None:
        raise TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, ConceptVariable.__class__.__name__
        )

    def as_type(self) -> None:
        raise TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, TypeVariable.__class__.__name__
        )

    def as_thing(self) -> None:
        raise TypeQLException.of(
            INVALID_CASTING, self.__class__.__name__, ThingVariable.__class__.__name__
        )

    @property
    def normalise(self):
        return self
    
    def is_variable(self) -> bool:
        return True
    
    def patterns(self) -> List:
        array = []
        # hope it's work
        return array.append(list(self))