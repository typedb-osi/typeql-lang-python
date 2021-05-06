
from abc import ABC

class ConceptVariableBuilder(ABC):

    @abstractmethod
    def iS(self, var):
        if type(var) is str:
            return self.iS(UnboudVariable.named(var))
        if type(var) is UnboundVariable:
            return self.constrain(ConceptConstraint.Is(var))

    @abstractmethod
    def constrain(self, constraint):
        pass