from abc import ABC, abstractmethod

class Variable(ABC):

    def __init__(self, reference):
        self._reference = reference
    
    @property
    @abstractmethod
    def constraints(self):
        pass
    
    @abstractmethod
    def is_unbound(self) -> bool:
        return False
    
    @abstractmethod
    def is_bound(self) -> bool:
        return False
    
    @abstractmethod
    def is_concept(self) -> bool:
        return False
    
    @abstractmethod
    def is_type(self) -> bool:
        return False

    @abstractmethod
    def is_thing(self) -> bool:
        return False
    
    @abstractmethod
    def as_unbound(self):
        raise # TODO

    @abstractmethod
    def as_bound(self):
        raise # TODO

    @abstractmethod
    def variables(self):
        pass

    @property
    @abstractmethod
    def kind():
        return self._reference.kind()

    @property
    @abstractmethod
    def name(self):
        if self._reference.kind() == NAME:
            return self._reference.as_name.name()
        else:
            return None
    
    @property
    @abstractmethod
    def reference(self):
        return self._reference

    @abstractmethod
    def is_named(self) -> bool:
        return self._reference.is_named()
    
    @abstractmethod
    def is_labelled(self) -> bool:
        return self._reference.is_labelled()

    @abstractmethod
    def is_anonymised(self) -> bool:
        return self._reference.is_anonymous()

    @abstractmethod
    def is_visible(self) -> bool:
        return self._reference.is_visible()
