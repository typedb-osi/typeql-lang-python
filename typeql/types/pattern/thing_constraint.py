import abc

class ThingConstraint(ConstraintT):

    @abc.abstractmethod
    def is_iid(self) -> bool:
        ...

    @abc.abstractmethod
    def is_isa(self) -> bool:
        ...

    @abc.abstractmethod
    def is_value(self) -> bool:
        ...
    
    @abc.abstractmethod
    def is_relation(self) -> bool:
        ...
    
    @abc.abstractmethod
    def is_relation(self) -> bool:
        ...
    
    @abc.abstractmethod
    def is_has(self) -> bool:
        ...
    
    @abc.abstractmethod
    def as_iid(self):
       ...
    
    @abc.abstractmethod
    def as_isa(self):
        ...

    @abc.abstractmethod
    def as_value(self):
        ...
    
    @abc.abstractmethod
    def as_relation(self):
        ...
    
    @abc.abstractmethod
    def as_has(self):
        ...
    