import abc


class VariableT(abc.ABC):

    def __init__(self, reference):
        self._reference = reference

   
    @abc.abstractmethod
    def constraints(self):
        ...

    @abc.abstractmethod
    def is_unbound(self) -> bool:
        ...

    @abc.abstractmethod
    def is_bound(self) -> bool:
        ...

    @abc.abstractmethod
    def is_concept(self) -> bool:
        ...

    @abc.abstractmethod
    def is_type(self) -> bool:
        ...

    @abc.abstractmethod
    def is_thing(self) -> bool:
        ...
    
    @abc.abstractmethod
    def as_unbound(self):
        ...

    @abc.abstractmethod
    def as_bound(self):
        ...

    @abc.abstractmethod
    def variables(self):
        ...

    @abc.abstractmethod
    def kind():
        ...

    @abc.abstractmethod
    def name(self):
        ...

    @abc.abstractmethod
    def reference(self):
        ...
    
    @abc.abstractmethod
    def is_named(self) -> bool:
        ...

    @abc.abstractmethod
    def is_labelled(self) -> bool:
        ...

    @abc.abstractmethod
    def is_anonymised(self) -> bool:
        ...

    @abc.abstractmethod
    def is_visible(self) -> bool:
        ...
