import abc

class ComputableT(abc.ABC):

    @abc.abstractmethod
    def method(self) -> 'MethodT':
        ...
    
    @abstractmethod
    def conditions_required(self):
        ...
    
    @abstractmethod
    def get_exception(self):
        ...

class Argument(abc.ABC):

    @abc.abstractmethod
    def type():
        ...
    
    @abc.abstractmethod
    def value():
        ...

class Arguments(abc.ABC):

    @abc.abstractmethod
    def min_K(self):
        ...
    
    @abc.abstractmethod
    def k(self):
        ...

    @abc.abstractmethod
    def size(self):
        ...
    
    @abc.abstractmethod
    def contains(self):
        ...

class DirectionalT(ComputableT):

    @abc.abstractmethod
    def from(self):
        ...

    @abc.abstractmethod
    def to(self):
        ...

class TargetableT(ComputableT):
    @abc.abstractmethod
    def of(self):
        ...

class ScopeableT(ComputableT):

    @abc.abstractmethod
    def in(self):
        ...

    @abc.abstractmethod
    def include_attributes(self) -> bool:
        ...
    
    @abc.abstractmethod
    def attributes(self) -> bool:
        ...

class ConfigurableT(ComputableT):

    @abc.abstractmethod
    def using(self) -> 'AlgorithmT':
        ...

    @abc.abstractmethod
    def where(self):
        ...
    
    @abc.abstractmethod
    def arguments_default(self):
        ...
    
    @abc.abstractmethod
    def algorithms_accepted(self):
        ...
    
    @abc.abstractmethod
    def arguments_accepted(self):
        ...