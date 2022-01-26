import abc

class ThingVariableBuilderT(abc.ABC):

    class Common(abc.ABC):

        @abc.abstractmethod
        def isa(self):
            ...
        
        @abc.abstractmethod
        def isaX(self):
            ...
        
        @abc.abstractmethod
        def isaX(self):
            ...       
            
        @abc.abstractmethod
        def has(self):
            ...
        
        @abc.abstractmethod
        def constrain(self):
            ...
    
    class Thing(abc.ABC):

        @abc.abstractmethod
        def iid(self, idd) -> ThingVariable.Thing:
            ...
        
        @abc.abstractmethod
        def constrain(self, constraint: ThingConstraint.IID) ->  ThingVariable.Thing:
            ...
        
    class Relation(abc.ABC):

        @abc.abstractmethod
        def rel(self):
            ...
        
        def constrain(self, constraint: ThingConstraint.IID) -> ThingVariable.Thing:
            ...
        
    class Attribute(abc.ABC):

        @abc.abstractmethod
        def eq(self):
            ...
        
        @abc.abstractmethod
        def neq(self):
            ...
          
        @abc.abstractmethod
        def gt(self):
            ...

        @abc.abstractmethod
        def gte(self):
            ...

        @abc.abstractmethod
        def lt(self):
            ...

        @abc.abstractmethod
        def lte(self):
            ...
        
        @abc.abstractmethod
        def lte(self):
            ...
        
        @abc.abstractmethod
        def constrains(self, value: str)->  ThingVariable.Attribute:
            ...
        
        @abc.abstractmethod
        def like(self, regex: str)->  ThingVariable.Attribute:
            ...
        