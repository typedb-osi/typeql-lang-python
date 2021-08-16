from _typeshed import SupportsWrite
from abc import ABC, abstractmethod
class Computable(ABC):

    @abstractmethod
    def method(self):
        pass
    
    @abstractmethod
    def conditions_required(self):
        pass
    
    @abstractmethod
    def get_exception(self):
        pass

    class Directional(Computable):

        # TODO add dispatcher
        @abstractmethod
        def from_(self, from_id: str) -> str:
            pass
        
        @abstractmethod
        def to(self, to_id: str) -> str:
            pass
        

      


class Argument(ABC):
    def _type():
        pass
    
    def value():
        pass

class Arguments(ABC):

    def _min_K():
        pass
    
    def _k():
        pass

    def _size():
        pass
    
    def _contains():
        pass


class Targetable(Computable):
    
    def of(self, type, types):
        pass
    

class Scopeable(Computable):

    def includes_attributes():
        pass
    
    def in(self, type, types):
        pass
    
    def attributes(self, include):
        pass

    class Configurable(Computable):
        
        @abstractmethod
        def using(self):
            pass
        
        @abstractmethod
        def where():
            pass
        
        @abstractmethod
        def algorithms_accepted():
            pass
        
        @abstractmethod
        def argumentes_default():
            pass