import abc

class TypeQLDefinable(TypeQLQueryT):

    @abc.abstractmethod
    def variables(self):
        ...
    
    @abc.abstractmethod
    def rules(self):
        ...
    
