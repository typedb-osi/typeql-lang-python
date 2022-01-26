
import abc

class TypeQLComputeT(TypeQLQueryT):

    @abc.abstractmethod
    def in(self):
        ...
    
    @abc.abstractmethod
    def includes_attributes(self) -> bool:
        ...
    
    @abc.abstractmethod
    def is_valid(self) -> bool:
        ...
    
    @abc.abstractmethod
    def _print_conditions(self) -> str:
        ...
    
    @abc.abstractmethod
    def _print_of(self) -> str:
        ...
    
    @abc.abstractmethod
    def _print_in(self) -> str:
        ...
    
    @abc.abstractmethod
    def _print_types(self) -> str:
        ...
    
    @abc.abstractmethod
    def _print_algorithm(self) -> str:
        ...
    
    @abc.abstractmethod
    def _print_arguments(self) -> str:
        ...

class Builder(abc.ABC):
    
        @abc.abstractmethod
        def count(self):
            ...

        @abc.abstractmethod
        def max(self):
            ...

        @abc.abstractmethod
        def min(self):
            ...

        @abc.abstractmethod
        def mean(self):
            ...

        @abc.abstractmethod
        def median(self):
            ...

        @abc.abstractmethod
        def sum(self):
            ...
            
        @abc.abstractmethod
        def std(self):
            ...

        @abc.abstractmethod
        def path(self):
            ...

        @abc.abstractmethod
        def centrality(self):
            ...

        @abc.abstractmethod
        def cluster(self):
            ...


class StatisticsT(TypeQLComputeT):

    @abc.abstractmethod
    def as_count(self):
        ...

    @abc.abstractmethod
    def as_value(self):
        ...


class CountT(StatisticsT):

        @abc.abstractmethod
        def in(self):
            ...

        @abc.abstractmethod
        def attributes(self):
            ...

        @abc.abstractmethod
        def conditions_required(self):
            ...

        @property
        @abc.abstractmethod
        def exception(self):
            ...

class ValueT(StatisticsT):
    
    @abc.abstractmethod
    def of(self, types: str):
        ... 

    @abc.abstractmethod
    def inside(self, types: str):
        ...

    @abc.abstractmethod
    def attributes(self, include: bool):
        ...

    @abc.abstractmethod
    def conditions_required(self):
        ...

    @abc.abstractmethod
    def exception(self):
        ...


class PathT(TypeQLComputeT):
    ...

class ConfigurableT(TypeQLComputeT):
    ...

class CentralityT(ConfigurableT):
    ...

class ClusterT(ConfigurableT):
    ...

class ArgumentT():
    ...