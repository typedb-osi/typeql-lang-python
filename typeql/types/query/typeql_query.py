import abc

class TypeQLQueryT(abc.ABC):

    @abc.abstractmethod
    def type(self):
        ...

    @abc.abstractmethod
    def as_define(self):
        ...
    
    @abc.abstractmethod
    def as_undefine(self):
       ...

    @abc.abstractmethod
    def as_insert(self):
        ...
    
    @abc.abstractmethod
    def as_delete(self):
        ...
    
    @abc.abstractmethod
    def as_update(self):
        ...

    @abc.abstractmethod
    def as_match(self):
        ...

    @abc.abstractmethod
    def as_match_aggregate(self):
        ...

    @abc.abstractmethod
    def as_match_group(self):
        ...

    @abc.abstractmethod
    def as_match_group_aggregate(self):
        ...

    @abc.abstractmethod
    def as_compute_statistics(self):
        ...

    @abc.abstractmethod
    def as_compute_path(self):
        ...

    @abc.abstractmethod
    def as_compute_centrality(self):
        ...

    @abc.abstractmethod
    def as_compute_cluster(self):
        ...

    @abc.abstractmethod
    def __str__(self) -> str:
        ...
    
    @abc.abstractmethod
    def __eq__(self) -> bool:
        ...