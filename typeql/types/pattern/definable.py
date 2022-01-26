import abc

class DefinableT(abc.ABC):

    @abc.abstractmethod
    def is_rule(self) -> bool:
        ...

    @abc.abstractmethod
    def is_type_variable(self) -> bool:
        ...

    @abc.abstractmethod
    def as_rule(self):
        ...

    @abc.abstractmethod
    def as_type_variable(self):
       ...
