class Aggregatable(TypeQLQuery):
    @abstracmethod
    def _aggregate(self, method, var):
        pass

    @abstracmethod
    def _count(self):
        return self._aggregate(COUNT, None)

    @abstracmethod
    def _max(self, var):
        if type(var) == str:
            var = UnboundVariable.named(var)
        return _aggregate(MAX, var)

    @abstracmethod
    def _mean(self, var):
        if type == str:
            var = UnboundVariable.named(var)
        return _aggregate(MEAN, var)

    @abstracmethod
    def _median(self, var):
        if type(var) == str:
            var = UnboundVariable.named(var)
        return _aggregate(MEDIAN, var)

    @abstracmethod
    def _min(self, var):
        if type(var) == str:
            var = UnboundVariable.named(var)
        return _aggregate(STD, var)

    @abstracmethod
    def _sum(self, var):
        if type(var) == str:
            var = UnboundVariable.named(var)
        return _aggregate(SUM, var)
