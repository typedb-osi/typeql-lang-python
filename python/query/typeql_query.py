from abc import ABC, abstractmethod

class TypeQLQuery(ABC):

    def as_define(self):
        if isinstance(self, TypeQLDefine):
            return self
        else:
            raise # TODO
    
    def as_undefine(self):
        if isinstance(self, TypeQLUndefine):
            return self
        else:
            raise # TODO

    def as_insert(self):
        if isinstance(self, TypeQLInsert):
            return self
        else:
            raise # TODO

    def as_delete(self):
        if isinstance(self, TypeQLDelete):
            return self
        else:
            raise # TODO
    
    def as_update(self):
        if isinstance(self, TypeQLUpdate):
            return self
        else:
            raise # TODO
    
    def as_match(self):
        if isinstance(self, TypeQLMatch):
            return self
        else:
            raise # TODO
    
    def as_match_aggregate(self):
        if isinstance(self, TypeQLMatch.Aggregate):
            return self
        else:
            raise # TODO
    
    def as_match_group(self):
        if isinstance(self, TypeQLMatch.Group):
            return self
        else:
            raise # TODO

    def as_match_group_aggregate(self):
        if isinstance(self, TypeQLMatch.Group.Aggregate):
            return self
        else:
            raise # TODO

    def as_compute_statistics(self):
        if isinstance(self, TypeQLCompute.Statistics):
            return self
        else:
            raise # TODO

    def as_compute_path(self):
        if isinstance(self, TypeQLCompute.Path):
            return self
        else:
            raise # TODO

    def as_compute_centrality(self):
        if isinstance(self, TypeQLCompute.Centrality):
            return self
        else:
            raise # TODO
        
    def as_compute_cluster(self):
        if isinstance(self, TypeQLCompute.Cluster):
            return self
        else:
            raise # TODO
    
    @abstractmethod
    def __str__(self):
        pass