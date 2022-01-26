import abc
from enum import Enum
    

class ReferenceT(abc.ABC):


    class Type(Enum):
        NAME = "NAME"
        LABEL = "LABEL"
        ANONYMOUS = "ANONYMOUS"

    @abc.abstractmethod
    def __init__(self, type: Type, is_visible: bool):
        self._type = type
        self._is_visible = is_visible

    @abc.abstractmethod
    def name(self, name: str):
        ...
    
    @abc.abstractmethod
    def label(self, label: str):
        ...
    
    @abc.abstractmethod
    def anonymous(self, is_visible: bool):
        ...

    @abc.abstractmethod
    def type(self):
        ...

    @abc.abstractmethod
    def is_visible(self) -> bool:
        ...

    @abc.abstractmethod
    def is_referable(self) -> bool:
        ...
    
    @abc.abstractmethod
    def is_name(self) -> bool:
        ...
    
    @abc.abstractmethod
    def is_label(self) -> bool:
        ...
    
    @abc.abstractmethod
    def is_anonymous(self) -> bool:
        ...
    
    @abc.abstractmethod
    def as_referable(self):
        ...
    
    @abc.abstractmethod
    def as_name(self):
        ...
    
    @abc.abstractmethod
    def as_label(self):
        ...

    @abc.abstractmethod
    def as_anonymous(self):
        ...


