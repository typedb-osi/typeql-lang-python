from abc import ABC, abstractmethod


class IThingVariableBuilder(ABC):

    class ICommon:

        @abstractmethod
        def isa(self, type, var):
            pass
        
        @abstractmethod
        def isaX(self, type):
            pass
        
        @abstractmethod
        def has(self, type, value):
            pass
        
        @abstractmethod
        def constraint(self):
            pass
    
    class IThing:

        @abstractmethod
        def iid(self, id):
            pass
        
        @abstractmethod
        def constraint(self, constraint):
            pass
        
    class IRelation:

        @abstractmethod
        def rel(self, roleType, playerVar):
            pass
        
        @abstractmethod
        def constrain(self, rolePlayer):
            pass
    
    class IAttribute:
        
        @abstractmethod
        def __eq__(self, other):
            pass

        def __ne__(self , other):
            pass
        
        def __ge__(self, other):
            pass
        
        def __gt__(self, other):
            pass
        
        def __lt__(self, other):
            pass
        
        def __le__(self, other):
            pass
        
        def constains(self, value):
            pass
        
        def like(self, regex)
            pass

        def constrain(self):
            pass
        

        