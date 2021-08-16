from query.typeql_query import TypeQLQuery
from pattern.variable.unbound_variable import UnboundVariable
from common.typeql_token import TypeQLToken
class Aggregatable(TypeQLQuery):
    def __init__(self, method, var):
        pass

    def count(self):
        return self._aggregate(TypeQLToken.Aggregate.Method.COUNT, None)

    def max(self, var):
        if type(var) == str:
            return self.max(UnboundVariable.named(var))
        return self._aggregate(TypeQLToken.Aggregate.Method.MAX, var)

    def mean(self, var):
        if type(var) == str:
            return self.mean(UnboundVariable.named(var))
        return self._aggregate(TypeQLToken.Aggregate.Method.MEAN, var)

    def median(self, var):
        if type(var) == str:
            return self.median(UnboundVariable.named(var))
        return self._aggregate(TypeQLToken.Aggregate.Method.MEDIAN, var)

    def min(self, var):
        if type(var) == str:
            return self.min(UnboundVariable.named(var))
        return self._aggregate(TypeQLToken.Aggregate.Method.STD, var)

    def sum(self, var):
        if type(var) == str:
            return self.sum(UnboundVariable.named(var))
        return self._aggregate(TypeQLToken.Aggregate.Method.SUM, var)

