import abc

class TypeConstraintT(ConstraintT):

    @abc.abstractmethod
    def is_label(self) -> bool:
        ...
    
    @abc.abstractmethod
    def is_sub(self) -> bool:
        ...
    
    @abc.abstractmethod
    def is_abstract(self) -> bool:
        ...
    
    @abc.abstractmethod
    def is_value_type(self) -> bool:
        ...
    
    @abc.abstractmethod
    def is_regex(self) -> bool:
        ...
    
    @abc.abstractmethod
    def is_owns(self) -> bool:
        ...
    
    @abc.abstractmethod
    def is_plays(self) -> bool:
        ...
    
    @abc.abstractmethod
    def is_relates(self) -> bool:
        ...
    
    @abc.abstractmethod
    def as_label(self):
        ...
    
    @abc.abstractmethod
    def as_sub(self):
        ...
    
    @abc.abstractmethod
    def as_abstract(self):
        ...
    
    @abc.abstractmethod
    def as_value_type(self):
        ...
    
    @abc.abstractmethod
    def as_regex(self):
        ...
    
    @abc.abstractmethod
    def as_owns(self):
        ...
    
    @abc.abstractmethod
    def as_relates(self):
        ...

    @abc.abstractmethod
    def __str__(self) -> str:
        ...

    @abc.abstractmethod
    def __eq__(self) -> bool:
       ...
    
    @abc.abstractmethod
    def __hash__(self):
       ...
    
class LabelT(TypeConstraintT):

    @property
    @abc.abstractmethod
    def scope(self):
        ...
    
    @property
    @abc.abstractmethod
    def label(self) -> str:
        ...

    @abc.abstractmethod
    def scoped_label(self) -> str:
        ...

class SubT(TypeConstraintT):

    @property
    @abc.abstractmethod
    def type(self) -> TypeVariable:
        ...
    
    @property
    @abc.abstractmethod
    def is_explicit(self) -> bool:
        ...
    

class AbstractT(TypeConstraintT):
    ...


class ValueTypeT(TypeConstraintT):
    ...

class RegexT(TypeConstraintT):
    ...

class OwnsT(TypeConstraintT):

    @property
    @abc.abstractmethod
    def attribute(self) -> TypeVariable:
        ...
    
    @property
    @abc.abstractmethod
    def overridden(self):
        ...
    
    @property
    @abc.abstractmethod
    def is_key(self) -> bool:
        ...

class PlaysT(TypeConstraintT):

    @abc.abstractmethod
    def relation(self):
        ...
    
    @property
    @abc.abstractmethod
    def role(self) -> TypeVariable:
        ...
    
    @abc.abstractmethod
    def overridden(self):
        ...

    @abc.abstractmethod
    def _scope_type(self):
        ...


class RelatesT(TypeConstraintT):

    @property
    @abc.abstractmethod
    def _scoped_type(self):
        ...
    
    @property
    @abc.abstractmethod
    def role(self) -> TypeVariable:
        ...
    
    @abc.abstractmethod
    def overridden(self):
        ...
