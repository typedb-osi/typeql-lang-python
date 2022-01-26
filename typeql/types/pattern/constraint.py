import abc

class ConstraintT(abc.ABC, BoundVariable):

    @abc.abstractmethod
    def variables(self):
        ...
    
    @abc.abstractmethod
    def is_concept(self) -> bool:
        ...

    @abc.abstractmethod
    def is_thing(self) -> bool:
        ...
    
    @abc.abstractmethod
    def as_concept(self):
        ...
    
    @abc.abstractmethod
    def as_type(self):
        ...

    @abc.abstractmethod
    def as_thing(self):
        ...
