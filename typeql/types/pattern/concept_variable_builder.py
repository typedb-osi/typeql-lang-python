import abc


class ConceptVariableBuilderT(abc.ABC):

    @abc.abstractmethod
    def is(self):
        ...

    @abstractmethod
    def constrain(self):
        ...